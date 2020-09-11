import networkx as nx
import matplotlib.pyplot as plt

from pickling import load_content_from_file
from config import load_config_dict_from_json_file
from objects import *

Entities_by_id = load_content_from_file()

config_dict = load_config_dict_from_json_file()
subnetwork_center = config_dict["subgraph_center"]
bacon_distance = config_dict["bacon_distance"]
blacklist = config_dict["blacklist"]
draw_networkx_graph = config_dict["draw_networkx_graph"]
output_gephi_file = config_dict["output_gephi_file"]

# construct subgraph

G = nx.DiGraph() # nx graph object; used are:
# .nodes attribute
# .add_edge and .remove_node methods (not .add_node)

subgraph_node_ids = [ ] # Entity objects
node_ids_to_append_this_time = subnetwork_center # list of 5-digit strings

for i in range( bacon_distance + 1 ):

	node_ids_to_append_next_time = []

	for id in node_ids_to_append_this_time:

		# append
		subgraph_node_ids.append(id)

		# don't do anything else for things on blacklist
		if id in blacklist: continue

		# create edges and queue up connected nodes for next time
		E = Entities_by_id[id]
		if E.type == 'work':

			for author_id in E.author_ids:
				node_ids_to_append_next_time.append( author_id )
				G.add_edge(author_id, E.id, arrowstyle = '-[')

			for base_text_id in E.base_text_ids:
				node_ids_to_append_next_time.append( base_text_id )
				G.add_edge(base_text_id, E.id, arrowstyle = '->')

			for commentary_id in E.commentary_ids:
				node_ids_to_append_next_time.append( commentary_id )
				G.add_edge(E.id, commentary_id, arrowstyle = '->')

		elif E.type == 'author':

			for work_id in E.work_ids:
				node_ids_to_append_next_time.append( work_id )
				G.add_edge(E.id, work_id, arrowstyle = '-[')

	# de-dupe, first list-internally, then against previous
	node_ids_to_append_next_time = list(set(node_ids_to_append_next_time))
	for id in node_ids_to_append_next_time:
		if id in subgraph_node_ids:
			node_ids_to_append_next_time.remove(id)

	node_ids_to_append_this_time = node_ids_to_append_next_time

# trim queued-up but unestablished periphery nodes

for n in list(G.nodes):
	if n not in subgraph_node_ids:
		G.remove_node(n)

# assign node labels and colors

node_ids = list(G.nodes)
label_map = {} # dict
color_map = [] # list
for node_id in node_ids:

	label_map[node_id] = Entities_by_id[node_id].name

	if Entities_by_id[node_id].id in blacklist:
		color_map.append('grey')

	elif Entities_by_id[node_id].type == 'work':
		color_map.append('red')

	elif Entities_by_id[node_id].type == 'author':
		color_map.append('green')

# output for Gephi

if output_gephi_file:

	# change primary labels to words instead of ID numbers
	G_relabled = nx.relabel_nodes(G, label_map)

	output_fn = "%s" % label_map[subnetwork_center[0]]
	if len(subnetwork_center) > 1:
		output_fn = output_fn + "_etc"
	output_fn = output_fn + "_degree_%d" % bacon_distance
	if blacklist != []:
		output_fn = output_fn + "_with_blacklist"
	output_fn = output_fn + ".gexf"

	nx.write_gexf(G_relabled, output_fn)

# draw networkx graph

if draw_networkx_graph:

	plt.figure(1,figsize=(14,7))
	nx.draw_spring(G, labels = label_map, node_color = color_map, node_size = 1000)
	plt.show()
