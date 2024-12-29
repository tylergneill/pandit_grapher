import csv
import json
import os

from data_models import Work, Author
from util import time_execution

current_file_dir = os.path.dirname(os.path.abspath(__file__))
relative_data_dir = "../data"

@time_execution
def create_entities():
    """
    Transform reduced CSV data to data.models.Entity objects stored in JSON.
    """

    input_filename = "2024-12-23-works-cleaned.csv"
    input_csv_path = os.path.join(current_file_dir, relative_data_dir, input_filename)

    entities_by_id = {}

    with open(input_csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            work_id = row["ID"]
            work_name = row["Title"]
            author_ids = [id.strip() for id in (row["Authors (IDs)"] or "").split(",") if id.strip()]
            author_names = [name.strip() for name in (row["Authors (names)"] or "").split(",") if name.strip()]
            base_text_ids = [id.strip() for id in (row["Base texts (IDs)"] or "").split(",") if id.strip()]
            base_text_names = [name.strip() for name in (row["Base texts (names)"] or "").split(",") if name.strip()]

            # Handle Work entity
            if work_id in entities_by_id:
                W = entities_by_id[work_id]
            else:
                W = Work(work_id)
                entities_by_id[work_id] = W
            W.name = work_name

            # Handle Author entities
            for author_id, author_name in zip(author_ids, author_names):
                if author_id in entities_by_id:
                    A = entities_by_id[author_id]
                else:
                    A = Author(author_id)
                    entities_by_id[author_id] = A
                A.name = author_name
                if W.id not in A.work_ids:
                    A.work_ids.append(W.id)
                if A.id not in W.author_ids:
                    W.author_ids.append(A.id)

            # Handle Base Text entities
            for base_text_id, base_text_name in zip(base_text_ids, base_text_names):
                if base_text_id in entities_by_id:
                    BT = entities_by_id[base_text_id]
                else:
                    BT = Work(base_text_id)
                    entities_by_id[base_text_id] = BT
                BT.name = base_text_name
                if W.id not in BT.commentary_ids:
                    BT.commentary_ids.append(W.id)
                if BT.id not in W.base_text_ids:
                    W.base_text_ids.append(BT.id)

    # Save to JSON for human-readability
    output_filename = "2024-12-23-entities.json"
    output_json_path = os.path.join(current_file_dir, relative_data_dir, output_filename)
    with open(output_json_path, 'w') as jsonfile:
        json.dump({eid: e.to_dict() for eid, e in entities_by_id.items()}, jsonfile, indent=4, ensure_ascii=False)

    return entities_by_id

@time_execution
def create_graph(entities_by_id):
    """
    Create full graph and save.
    """

    # Initialize the graph structure
    graph = {
        "nodes": [],
        "edges": []
    }

    # Track added nodes to avoid duplication
    added_nodes = set()

    # Populate nodes and edges
    for entity_id, entity in entities_by_id.items():
        # Add node
        if entity_id not in added_nodes:
            graph["nodes"].append({
                "id": entity_id,
                "label": entity.name,
                "type": entity.type  # 'work' or 'author'
            })
            added_nodes.add(entity_id)

        # Add edges based on relationships
        if entity.type == "work":
            # Author relationships
            for author_id in entity.author_ids:
                graph["edges"].append({
                    "source": author_id,
                    "target": entity_id,
                    "relationship": "author"
                })

            # Base text relationships
            for base_text_id in entity.base_text_ids:
                graph["edges"].append({
                    "source": base_text_id,
                    "target": entity_id,
                    "relationship": "base_text"
                })

            # Commentary relationships
            for commentary_id in entity.commentary_ids:
                graph["edges"].append({
                    "source": entity_id,
                    "target": commentary_id,
                    "relationship": "commentary"
                })

        elif entity.type == "author":
            # Work relationships
            for work_id in entity.work_ids:
                graph["edges"].append({
                    "source": entity_id,
                    "target": work_id,
                    "relationship": "author"
                })

    # Save to JSON for human-readability
    output_filename = "2024-12-23-graph.json"
    output_json_path = os.path.join(current_file_dir, relative_data_dir, output_filename)
    with open(output_json_path, 'w') as jsonfile:
        json.dump(graph, jsonfile, indent=4, ensure_ascii=False)

entities_by_id = create_entities()
create_graph(entities_by_id)
