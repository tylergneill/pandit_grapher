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
        {"id": "1", "label": "Node 1"},
        {"id": "2", "label": "Node 2"},
        {"id": "3", "label": "Node 3"},
    ],
    "edges": [
        {"source": "1", "target": "2", "relationship": "author"},
        {"source": "2", "target": "3", "relationship": "commentary"},
    ]
}

# --- Subgraph Endpoint ---
@ns.route('/subgraph')
class Subgraph(Resource):
    @ns.expect(subgraph_model)
    def post(self):
        data = request.json
        # Simulate filtering logic (currently mock data)
        return jsonify({"graph": mock_graph})

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
