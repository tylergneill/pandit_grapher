from flask import Flask, render_template, Blueprint, jsonify, request
from flask_restx import Api, Resource, fields

from convert import convert_to_mock_graph
from grapher import construct_subgraph
from pickling import load_content_from_file

Entities_by_id = load_content_from_file()

app = Flask(__name__)

# --- Blueprint Setup ---
api_bp = Blueprint('api', __name__, url_prefix='/api')  # API Blueprint
api = Api(api_bp, version='1.0', title='PANDiT Grapher API',
          description='API for exploring PANDiT project graphs',
          doc='/docs')  # Swagger UI available at /api/docs

# --- Define Namespace ---
ns = api.namespace('graph', description='Graph operations')

# --- Request Model ---
subgraph_model = api.model('SubgraphRequest', {
    'subgraph_center': fields.List(fields.String, required=True, description='List of center node IDs'),
    'hops': fields.Integer(required=True, description='Number of hops outward from center'),
    'blacklist': fields.List(fields.String, required=False, description='List of node IDs to exclude')
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

@ns.route('/all-entities')
class DropdownOptions(Resource):
    def get(self):
        """Fetch dropdown options for nodes."""
        dropdown_options = [{"id": node["id"], "label": f"{node['label']} ({node['id']})"} for node in mock_graph["nodes"]]
        return jsonify(dropdown_options)

@ns.route('/subgraph')
class Subgraph(Resource):
    @ns.expect(subgraph_model)
    def post(self):
        """
        Generate a subgraph based on input parameters.
        """
        try:
            # Parse request data
            data = request.json
            subgraph_center = set(data.get('subgraph_center', []))
            hops = data.get('hops', 0)
            blacklist = set(data.get('blacklist', []))

            # Validate inputs
            if not subgraph_center:
                return {"error": "subgraph_center must be a non-empty list"}, 400
            if not isinstance(hops, int) or hops < 0:
                return {"error": "hops must be a non-negative integer"}, 400
            if not isinstance(blacklist, set):
                return {"error": "blacklist must be a list"}, 400

            # Call the actual construct_subgraph function
            Pandit_Graph = construct_subgraph(list(subgraph_center), hops, list(blacklist))

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
                    "subgraph_center": list(subgraph_center),
                    "hops": hops,
                    "blacklist": list(blacklist)
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
api.add_namespace(ns)

# Register the Blueprint
app.register_blueprint(api_bp)

# --- Frontend Route ---
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5090)
