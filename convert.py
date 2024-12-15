from pickling import load_content_from_file

def convert_to_mock_graph():
    # Load the pickled Entities_by_id data
    Entities_by_id = load_content_from_file()

    # Initialize the mock graph structure
    mock_graph = {
        "nodes": [],
        "edges": []
    }

    # Track added nodes to avoid duplication
    added_nodes = set()

    # Populate nodes and edges
    for entity_id, entity in Entities_by_id.items():
        # Add node
        if entity_id not in added_nodes:
            mock_graph["nodes"].append({
                "id": entity_id,
                "label": entity.name,
                "type": entity.type  # 'work' or 'author'
            })
            added_nodes.add(entity_id)

        # Add edges based on relationships
        if entity.type == "work":
            # Author relationships
            for author_id in entity.author_ids:
                mock_graph["edges"].append({
                    "source": author_id,
                    "target": entity_id,
                    "relationship": "author"
                })

            # Base text relationships
            for base_text_id in entity.base_text_ids:
                mock_graph["edges"].append({
                    "source": base_text_id,
                    "target": entity_id,
                    "relationship": "base_text"
                })

            # Commentary relationships
            for commentary_id in entity.commentary_ids:
                mock_graph["edges"].append({
                    "source": entity_id,
                    "target": commentary_id,
                    "relationship": "commentary"
                })

        elif entity.type == "author":
            # Work relationships
            for work_id in entity.work_ids:
                mock_graph["edges"].append({
                    "source": entity_id,
                    "target": work_id,
                    "relationship": "author"
                })

    return mock_graph
