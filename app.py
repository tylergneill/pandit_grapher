from flask import Flask, render_template, Blueprint, jsonify, request
from flask_restx import Api, Resource, fields

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


@ns.route('/dropdown-options')
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
        data = request.json
        subgraph_center = set(data.get('subgraph_center', []))
        hops = data.get('hops', 0)
        blacklist = set(data.get('blacklist', []))

        # Initialize BFS data structures
        included_nodes = set(subgraph_center)
        included_edges = set()  # Use a set to avoid duplicates
        frontier = subgraph_center  # Nodes to explore in the current hop

        for _ in range(hops):  # Perform BFS up to the specified hops
            next_frontier = set()
            for edge in mock_graph["edges"]:
                if edge["source"] in frontier and edge["target"] not in blacklist:
                    included_edges.add((edge["source"], edge["target"], edge["relationship"]))
                    next_frontier.add(edge["target"])
                elif edge["target"] in frontier and edge["source"] not in blacklist:
                    included_edges.add((edge["source"], edge["target"], edge["relationship"]))
                    next_frontier.add(edge["source"])
            frontier = next_frontier - included_nodes  # Prevent revisiting nodes
            included_nodes.update(next_frontier)

        # Filter nodes based on inclusion
        filtered_nodes = [node for node in mock_graph["nodes"] if node["id"] in included_nodes]

        # Convert edges back to list of dicts
        filtered_edges = [{"source": src, "target": tgt, "relationship": rel} for src, tgt, rel in included_edges]

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
