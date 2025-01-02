from collections import defaultdict

from flask import Flask, render_template, Blueprint, jsonify, request, send_from_directory, Response
from flask_restx import Api, Resource, fields

from grapher import construct_subgraph, annotate_graph
from utils.utils import find_app_version, find_data_version
from utils.load import load_entities

ENTITIES_BY_ID = load_entities()
APP_VERSION = find_app_version()
DATA_VERSION = find_data_version()

app = Flask(__name__)

# --- Blueprint setup ---
api_bp = Blueprint('api', __name__, url_prefix='/api')  # API Blueprint
api = Api(api_bp, version=APP_VERSION, title='Pandit Grapher API',
          description=f'API for exploring work and author relationships in Pandit database ({DATA_VERSION})',
          doc='/docs')  # Swagger UI available at /api/docs

# --- Define all namespaces ---
entities_ns = api.namespace('entities', description='Entity operations')
graph_ns = api.namespace('graph', description='Graph operations')

# --- entities namespace routes ---

# --- Preprocess EntitiesByType data ---
entity_dropdown_options = defaultdict(list)
for entity in ENTITIES_BY_ID.values():
    option = {"id": entity.id, "label": f"{entity.name} ({entity.id})"}
    entity_dropdown_options['all'].append(option)
    entity_dropdown_options[entity.type+'s'].append(option)

@entities_ns.route('/<string:entity_type>')
class EntitiesByType(Resource):
    def get(self, entity_type):
        """
        Fetch list of available IDs for a specific type of node (authors, works, or all).
        Example: /api/entities/works
        """
        if entity_type not in ['authors', 'works', 'all']:
            return jsonify({"error": "Invalid entity type. Choose from 'authors', 'works', or 'all'."}), 400

        return jsonify(entity_dropdown_options[entity_type])

@entities_ns.route('/labels')
class Labels(Resource):
    @api.doc(
        params={
            'ids': 'Comma-separated list of entity IDs to fetch labels for (e.g., 89000,12345)'
        },
        responses={
            200: 'Labels returned successfully',
            400: 'No IDs provided or other error',
            500: 'Internal server error'
        },
    )
    def get(self):
        """
        Fetch labels for a list of node IDs.
        Example: /api/entities/labels?ids=89000,12345
        """
        try:
            ids_param = request.args.get('ids')  # Get all IDs as a list
            ids = [id.strip() for id in ids_param.split(',')] if ids_param else []
            if not ids:
                return {"error": "No IDs provided"}, 400

            label_data = [
                {"id": node_id, "label": ENTITIES_BY_ID[node_id].name}
                for node_id in ids if node_id in ENTITIES_BY_ID
            ]

            return jsonify(label_data)
        except Exception as e:
            return {"error": str(e)}, 500

# register entities namespace
api.add_namespace(entities_ns)

# --- graph namespace routes ---

# --- Define request model for primary Subgraph endpoint ---
subgraph_model = api.model('SubgraphRequest', {
    'authors': fields.List(fields.String, required=False, description='List of author node IDs', example=[]),
    'works': fields.List(fields.String, required=False, description='List of work node IDs', example=["89000"]),
    'hops': fields.Integer(required=True, description='Number of hops outward from center', example=2),
    'exclude_list': fields.List(fields.String, required=False, description='List of node IDs to exclude', example=[])
})

def validate_inputs(authors, works, hops, exclude_list):
    if not authors and not works:
        return {"error": "require either one or both of authors or works"}, 400
    if not isinstance(hops, int) or hops < 0:
        return {"error": "hops must be a non-negative integer"}, 400
    if not isinstance(exclude_list, list):
        return {"error": "exclude_list must be a list"}, 400
    return "", 200

@graph_ns.route('/subgraph')
class Subgraph(Resource):
    @graph_ns.expect(subgraph_model)
    def post(self):
        """
        Generate a subgraph based on input parameters.
        """
        try:
            # Parse request data
            data = request.json
            authors = set(data.get('authors', []))
            works = set(data.get('works', []))
            subgraph_center = list(authors | works)  # union
            hops = data.get('hops', 0)
            exclude_list = list(set(data.get('exclude_list', [])))

            # validate_inputs
            msg_dict, status_code = validate_inputs(authors, works, hops, exclude_list)
            if status_code != 200:
                return msg_dict, status_code

            # Call the actual construct_subgraph function
            subgraph = construct_subgraph(subgraph_center, hops, exclude_list)
            annotated_subgraph = annotate_graph(subgraph, subgraph_center, exclude_list)

            # Extract nodes and edges
            filtered_nodes = [
                {
                    "id": node,
                    "label": ENTITIES_BY_ID[node].name,
                    "type": ENTITIES_BY_ID[node].type,
                    "is_central": annotated_subgraph.nodes[node].get('is_central', False),
                    "is_excluded": annotated_subgraph.nodes[node].get('is_excluded', False),
                }
                for node in annotated_subgraph.nodes
            ]
            filtered_edges = [
                {"source": edge[0], "target": edge[1], "relationship": "related"}
                for edge in subgraph.edges
            ]

            # Construct the response
            response = {
                "parameters": {
                    "authors": list(authors),
                    "works": list(works),
                    "hops": hops,
                    "exclude_list": list(exclude_list),
                },
                "graph": {
                    "nodes": filtered_nodes,
                    "edges": filtered_edges,
                }
            }
            return jsonify(response)

        except KeyError as e:
            app.logger.error('Error: %s', str(e))
            return {"error": f"Invalid ID: {str(e)}"}, 400
        except Exception as e:
            app.logger.error('Error: %s', str(e))
            return {"error": str(e)}, 500

@graph_ns.route('/render')
class RenderGraph(Resource):
    def get(self):
        """
        Return graph data as JSON.
        """
        try:
            # Parse parameters
            authors_param = request.args.getlist('authors')
            if len(authors_param) == 1 and ',' in authors_param[0]:
                authors_param = authors_param[0].split(',')
            authors = set(authors_param)

            works_param = request.args.getlist('works')
            if len(works_param) == 1 and ',' in works_param[0]:
                works_param = works_param[0].split(',')
            works = set(works_param)

            subgraph_center = authors | works

            hops = request.args.get('hops', default=2, type=int)
            exclude_list_param = request.args.getlist('exclude_list')
            if len(exclude_list_param) == 1 and ',' in exclude_list_param[0]:
                exclude_list_param = exclude_list_param[0].split(',')
            exclude_list = list(set(exclude_list_param))

            # Validate inputs
            msg_dict, status_code = validate_inputs(authors, works, hops, exclude_list)
            if status_code != 200:
                return msg_dict, status_code

            subgraph = construct_subgraph(subgraph_center, hops, exclude_list)

            # Extract nodes and edges for JSON response
            filtered_nodes = [
                {"id": node, "label": ENTITIES_BY_ID[node].name, "type": ENTITIES_BY_ID[node].type}
                for node in subgraph.nodes
            ]
            filtered_edges = [
                {"source": edge[0], "target": edge[1]}
                for edge in subgraph.edges
            ]

            return jsonify({"nodes": filtered_nodes, "edges": filtered_edges})
        except KeyError as e:
            app.logger.error('Error: %s', str(e))
            return {"error": f"Invalid ID: {str(e)}"}, 400
        except Exception as e:
            app.logger.error('Error: %s', str(e))
            return {"error": str(e)}, 500

# register graph namespace
api.add_namespace(graph_ns)

# --- frontend routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/notes/author')
def author_notes():
    return render_template('notes/author.html')

@app.route('/notes/data')
def data_notes():
    return render_template('notes/data.html')

@app.route('/notes/license')
def license_notes():
    return render_template('notes/license.html')

@app.route('/notes/technical')
def tech_notes():
    return render_template('notes/technical.html')

# --- data serving route ---
@app.route('/data/<path:filepath>')
def data(filepath):
    return send_from_directory('data', filepath)

# Register the Blueprint
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5090)
