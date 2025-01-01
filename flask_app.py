from flask import Flask, render_template, Blueprint, jsonify, request, send_from_directory
from flask_restx import Api, Resource, fields

from grapher import construct_subgraph
from utils.load import load_entities

entities_by_id = load_entities()

all_entity_dropdown_options = []
work_dropdown_options = []
author_dropdown_options = []
for entity in entities_by_id.values():
    option = {"id": entity.id, "label": f"{entity.name} ({entity.id})"}
    all_entity_dropdown_options.append(option)
    if entity.type == 'work':
        work_dropdown_options.append(option)
    elif entity.type == 'author':
        author_dropdown_options.append(option)

app = Flask(__name__)

# --- Blueprint Setup ---
api_bp = Blueprint('api', __name__, url_prefix='/api')  # API Blueprint
api = Api(api_bp, version='1.0', title='Pandit Grapher API',
          description='API for exploring Pandit work and author relationships',
          doc='/docs')  # Swagger UI available at /api/docs

# --- Define Namespace ---
graph_ns = api.namespace('graph', description='Graph operations')
entities_ns = api.namespace('entities', description='Entity operations')

# --- Request Model ---
subgraph_model = api.model('SubgraphRequest', {
    'authors': fields.List(fields.String, required=False, description='List of author node IDs'),
    'works': fields.List(fields.String, required=False, description='List of work node IDs'),
    'hops': fields.Integer(required=True, description='Number of hops outward from center'),
    'exclude_list': fields.List(fields.String, required=False, description='List of node IDs to exclude')
})

@entities_ns.route('/<string:entity_type>')
class EntityOptions(Resource):
    def get(self, entity_type):
        """Fetch dropdown options for a specific type of node (authors, works, or all)."""
        if entity_type not in ['authors', 'works', 'all']:
            return jsonify({"error": "Invalid entity type. Choose from 'authors', 'works', or 'all'."}), 400

        if entity_type == 'authors':
            dropdown_options = author_dropdown_options
        elif entity_type == 'works':
            dropdown_options = work_dropdown_options
        else:  # entity_type == 'all'
            dropdown_options = all_entity_dropdown_options

        return jsonify(dropdown_options)

@entities_ns.route('/metadata')
class Metadata(Resource):
    def get(self):
        """
        Fetch metadata for a list of node IDs.
        Example: /api/entities/metadata?ids=89000&ids=12345
        """
        try:
            ids = request.args.getlist('ids')  # Get all IDs as a list
            if not ids:
                return {"error": "No IDs provided"}, 400

            metadata = [
                {"id": node_id, "label": entities_by_id[node_id].name}
                for node_id in ids if node_id in entities_by_id
            ]

            return jsonify(metadata)
        except Exception as e:
            return {"error": str(e)}, 500

# --- Frontend Route ---
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

# Serve files from the "data" folder
@app.route('/data/<path:filepath>')
def data(filepath):
    return send_from_directory('data', filepath)

def validate_inputs(authors, works, hops, exclude_list):
    if not authors and not works:
        return {"error": "require either one or both of authors or works"}, 400
    if not isinstance(hops, int) or hops < 0:
        return {"error": "hops must be a non-negative integer"}, 400
    if not isinstance(exclude_list, set):
        return {"error": "exclude_list must be a list"}, 400
    return "", 200

@graph_ns.route('/render')
class RenderGraph(Resource):
    def get(self):
        """
        Return graph data as JSON.
        """
        try:
            # Parse parameters
            authors = set(request.args.getlist('authors'))
            works = set(request.args.getlist('works'))
            subgraph_center = authors | works  # union
            hops = request.args.get('hops', default=2, type=int)
            exclude_list = set(request.args.get('exclude_list'))

            # validate_inputs
            msg_dict, status_code = validate_inputs(authors, works, hops, exclude_list)
            if status_code != 200:
                return msg_dict, status_code

            subgraph = construct_subgraph(entities_by_id, subgraph_center, hops, exclude_list)

            # Extract nodes and edges for JSON response
            filtered_nodes = [
                {"id": node, "label": entities_by_id[node].name, "type": entities_by_id[node].type}
                for node in subgraph.nodes
            ]
            filtered_edges = [
                {"source": edge[0], "target": edge[1]}
                for edge in subgraph.edges
            ]

            return jsonify({"nodes": filtered_nodes, "edges": filtered_edges})
        except KeyError as e:
            return {"error": f"Invalid ID: {str(e)}"}, 400
        except Exception as e:
            return {"error": str(e)}, 500


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
            subgraph_center = authors | works  # union
            hops = data.get('hops', 0)
            exclude_list = set(data.get('exclude_list', []))

            # validate_inputs
            msg_dict, status_code = validate_inputs(authors, works, hops, exclude_list)
            if status_code != 200:
                return msg_dict, status_code

            # Call the actual construct_subgraph function
            subgraph = construct_subgraph(entities_by_id, list(subgraph_center), hops, list(exclude_list))

            # Extract nodes and edges
            filtered_nodes = [
                {"id": node, "label": entities_by_id[node].name, "type": entities_by_id[node].type}
                for node in subgraph.nodes
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
            return {"error": f"Invalid ID: {str(e)}"}, 400
        except Exception as e:
            return {"error": str(e)}, 500

# Add namespace to the API
api.add_namespace(graph_ns)
api.add_namespace(entities_ns)

# Register the Blueprint
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5090)
