from flask import Flask, render_template, Blueprint, jsonify, request
from flask_restx import Api, Resource, fields

from convert import convert_to_mock_graph
from grapher import construct_subgraph
from pickling import load_content_from_file

Entities_by_id = load_content_from_file()
Works_by_id = {k:v for k,v in Entities_by_id.items() if v.type == 'work'}
Authors_by_id = {k:v for k,v in Entities_by_id.items() if v.type == 'author'}

app = Flask(__name__)

# --- Blueprint Setup ---
api_bp = Blueprint('api', __name__, url_prefix='/api')  # API Blueprint
api = Api(api_bp, version='1.0', title='PANDiT Grapher API',
          description='API for exploring PANDiT project graphs',
          doc='/docs')  # Swagger UI available at /api/docs

# --- Define Namespace ---
graph_ns = api.namespace('graph', description='Graph operations')
entities_ns = api.namespace('entities', description='Entity operations')

# --- Request Model ---
subgraph_model = api.model('SubgraphRequest', {
    'authors': fields.List(fields.String, required=False, description='List of author node IDs'),
    'works': fields.List(fields.String, required=False, description='List of work node IDs'),
    # TODO: manually enforce that at least one is required
    'hops': fields.Integer(required=True, description='Number of hops outward from center'),
    'exclude_list': fields.List(fields.String, required=False, description='List of node IDs to exclude')
})

# --- Mock Data ---
mock_graph = {
    "nodes": [
        {"id": "1", "label": "Node 1", "type": "author"},
        {"id": "2", "label": "Node 2", "type": "work"},
        {"id": "3", "label": "Node 3", "type": "work"},
        {"id": "4", "label": "Node 4", "type": "work"},
        {"id": "5", "label": "Node 5", "type": "author"},
        {"id": "6", "label": "Node 6", "type": "work"},
        {"id": "7", "label": "Node 7", "type": "work"},
        {"id": "8", "label": "Node 8", "type": "author"},
        {"id": "9", "label": "Node 9", "type": "work"}
    ],
    "edges": [
        {"source": "1", "target": "2", "relationship": "author"},
        {"source": "2", "target": "3", "relationship": "commentary"},
        {"source": "3", "target": "4", "relationship": "base_text"},
        {"source": "4", "target": "5", "relationship": "author"},
        {"source": "5", "target": "6", "relationship": "commentary"},
        {"source": "6", "target": "7", "relationship": "base_text"},
        {"source": "7", "target": "8", "relationship": "author"},
        {"source": "8", "target": "9", "relationship": "commentary"},
        {"source": "9", "target": "1", "relationship": "base_text"}
    ]
}

mock_graph = convert_to_mock_graph()

@entities_ns.route('/<string:entity_type>')
class EntityOptions(Resource):
    def get(self, entity_type):
        """Fetch dropdown options for a specific type of node (authors, works, or all)."""
        if entity_type not in ['authors', 'works', 'all']:
            return jsonify({"error": "Invalid entity type. Choose from 'authors', 'works', or 'all'."}), 400

        if entity_type == 'authors':
            filtered_nodes = [node for node in mock_graph["nodes"] if node["type"] == "author"]
        elif entity_type == 'works':
            filtered_nodes = [node for node in mock_graph["nodes"] if node["type"] == "work"]
        else:  # entity_type == 'all'
            filtered_nodes = mock_graph["nodes"]

        dropdown_options = [{"id": node["id"], "label": f"{node['label']} ({node['id']})"} for node in filtered_nodes]
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
                {"id": node_id, "label": Entities_by_id[node_id].name}
                for node_id in ids if node_id in Entities_by_id
            ]

            return jsonify(metadata)
        except Exception as e:
            return {"error": str(e)}, 500

# --- Frontend Route ---
@app.route('/')
def index():
    return render_template('index.html')

@graph_ns.route('/render')
class RenderGraph(Resource):
    def get(self):
        """
        Test returning graph data as JSON.
        """
        try:
            # Parse parameters
            works = request.args.getlist('works')  # Accept multiple works
            hops = request.args.get('hops', default=2, type=int)

            # Validate inputs
            if not works:
                return {"error": "At least one work must be specified"}, 400
            if hops < 0:
                return {"error": "Hops must be a non-negative integer"}, 400

            # Construct graph with a single work as the center
            subgraph_center = works
            Pandit_Graph = construct_subgraph(subgraph_center, hops, [])

            # Extract nodes and edges for JSON response
            filtered_nodes = [
                {"id": node, "label": Entities_by_id[node].name, "type": Entities_by_id[node].type}
                for node in Pandit_Graph.nodes
            ]
            filtered_edges = [
                {"source": edge[0], "target": edge[1]}
                for edge in Pandit_Graph.edges
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
            subgraph_center = authors | works
            hops = data.get('hops', 0)
            exclude_list = set(data.get('exclude_list', []))

            # Validate inputs
            if not subgraph_center:
                return {"error": "subgraph_center must be a non-empty list"}, 400
            if not isinstance(hops, int) or hops < 0:
                return {"error": "hops must be a non-negative integer"}, 400
            if not isinstance(exclude_list, set):
                return {"error": "exclude_list must be a list"}, 400

            # Call the actual construct_subgraph function
            Pandit_Graph = construct_subgraph(list(subgraph_center), hops, list(exclude_list))

            # Extract nodes and edges
            filtered_nodes = [
                {"id": node, "label": Entities_by_id[node].name, "type": Entities_by_id[node].type}
                for node in Pandit_Graph.nodes
            ]
            filtered_edges = [
                {"source": edge[0], "target": edge[1], "relationship": "related"}
                for edge in Pandit_Graph.edges
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
                    "edges": filtered_edges
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
