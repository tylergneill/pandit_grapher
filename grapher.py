from copy import deepcopy
from typing import Dict

import networkx as nx
import matplotlib.pyplot as plt

from data_models import Entity
from config import load_config_dict_from_json_file
from objects import *
from utils.load import load_entities
from utils.utils import time_execution

config_dict = load_config_dict_from_json_file()
DEFAULT_AUTHORS = config_dict["authors"]
DEFAULT_WORKS = config_dict["works"]
DEFAULT_HOPS = config_dict["hops"]
DEFAULT_EXCLUDE_LIST = config_dict["exclude_list"]
draw_networkx_graph = config_dict["draw_networkx_graph"]
networkx_figure_size = config_dict["networkx_figure_size"]
output_gephi_file = config_dict["output_gephi_file"]

ENTITIES_BY_ID = load_entities()


@time_execution
def construct_subgraph(
	subgraph_center: set = DEFAULT_AUTHORS+DEFAULT_WORKS,
	hops: int = DEFAULT_HOPS,
	exclude_list: set = DEFAULT_EXCLUDE_LIST,
	entities_by_id: Dict[str, Entity] = ENTITIES_BY_ID,
):

	subgraph = nx.DiGraph() # nx graph object; used are:
	# .nodes attribute
	# .add_edge and .remove_node methods (not .add_node)

	subgraph_node_ids = [ ] # Entity objects
	node_ids_to_append_this_time = subgraph_center # list of 5-digit strings

	for i in range( hops + 1 ):

		node_ids_to_append_next_time = []

		for id in node_ids_to_append_this_time:

			# append
			subgraph_node_ids.append(id)

			# don't do anything else for things on exclude_list
			if id in exclude_list: continue

			# create edges and queue up connected nodes for next time
			E = entities_by_id[id]
			if E.type == 'work':

				for author_id in E.author_ids:
					node_ids_to_append_next_time.append( author_id )
					subgraph.add_edge(author_id, E.id, arrowstyle = '-[')

				for base_text_id in E.base_text_ids:
					node_ids_to_append_next_time.append( base_text_id )
					subgraph.add_edge(base_text_id, E.id, arrowstyle = '->')

				for commentary_id in E.commentary_ids:
					node_ids_to_append_next_time.append( commentary_id )
					subgraph.add_edge(E.id, commentary_id, arrowstyle = '->')

				if E.author_ids == E.base_text_ids == E.commentary_ids == []:
					subgraph.add_node(E.id)

			elif E.type == 'author':

				for work_id in E.work_ids:
					node_ids_to_append_next_time.append( work_id )
					subgraph.add_edge(E.id, work_id, arrowstyle = '-[')

				if E.work_ids == []:
					subgraph.add_node(E.id)

		# de-dupe, first list-internally, then against previous
		node_ids_to_append_next_time = list(set(node_ids_to_append_next_time))
		for id in node_ids_to_append_next_time:
			if id in subgraph_node_ids:
				node_ids_to_append_next_time.remove(id)

		node_ids_to_append_this_time = node_ids_to_append_next_time

	# trim queued-up but unestablished periphery nodes

	for n in list(subgraph.nodes):
		if n not in subgraph_node_ids:
			subgraph.remove_node(n)

	return subgraph

def assign_node_labels_and_colors(subgraph):

	node_ids = list(subgraph.nodes)
	label_map = {} # dict
	color_map = [] # list
	for node_id in node_ids:

		label_map[node_id] = ENTITIES_BY_ID[node_id].name

		if ENTITIES_BY_ID[node_id].id in DEFAULT_EXCLUDE_LIST:
			color_map.append('gray')

		elif ENTITIES_BY_ID[node_id].type == 'work':
			color_map.append('red')

		elif ENTITIES_BY_ID[node_id].type == 'author':
			color_map.append('green')

	return label_map, color_map

def export_to_gephi(subgraph, label_map, color_map, output_fn="pandit_grapher_output.gexf"):
    """
    Export a NetworkX graph to a GEXF file for Gephi with proper node labels and colors.
    """
    rgb_map = {
        "red": {'r': 255, 'g': 0, 'b': 0},
        "green": {'r': 6, 'g': 200, 'b': 50},
        "gray": {'r': 128, 'g': 128, 'b': 128},
    }

    # Create a deep copy of the graph to modify safely
    gexf_graph = deepcopy(subgraph)

    # Add labels and visualization attributes
    for i, node_id in enumerate(gexf_graph.nodes):
        gexf_graph.nodes[node_id]["label"] = label_map.get(node_id, f"Node {node_id}")
        if color_map[i] in rgb_map:
            gexf_graph.nodes[node_id]['viz'] = {
                'color': rgb_map[color_map[i]]
            }

    # Write the graph to a GEXF file
    nx.write_gexf(gexf_graph, output_fn, version="1.2draft")
    print(f"GEXF file exported to {output_fn}")

def draw_nx_graph(subgraph, label_map, color_map):
	plt.figure(1,figsize=tuple(networkx_figure_size))
	nx.draw_spring(subgraph, labels = label_map, node_color = color_map, node_size = 1000)
	plt.show()


if __name__ == "__main__":

	subgraph = construct_subgraph(DEFAULT_AUTHORS + DEFAULT_WORKS, DEFAULT_HOPS, DEFAULT_EXCLUDE_LIST)

	label_map, color_map = assign_node_labels_and_colors(subgraph)

	if output_gephi_file:
		export_to_gephi(subgraph, label_map, color_map)

	if draw_networkx_graph:
		draw_nx_graph(subgraph, label_map, color_map)
