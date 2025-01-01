import grapher

subgraph = grapher.construct_subgraph((grapher.ENTITIES_BY_ID.keys()), 1)
label_map, color_map = grapher.assign_node_labels_and_colors(subgraph)
grapher.export_to_gephi(subgraph, label_map, color_map, "complete_graph.gexf")
