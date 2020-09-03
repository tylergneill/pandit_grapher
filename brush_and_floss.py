import re

from pickling import save_content_to_file
from config import load_config_dict_from_json_file
from objects import *

config_dict = load_config_dict_from_json_file()
work_CSV_fn = config_dict["work_CSV_fn"]

# read in and clean Work CSV data

CSV_data = open(work_CSV_fn,'r').read()

# collapse long text fields (i.e., ones with internal newlines, tabs)
# so that they don't mess up table
cleaning_replacements = [ (r'[\t\n]{2,}', r' '), (r'\n([^"])', r' \1') ]
for c_r in cleaning_replacements:
	CSV_data = re.sub(c_r[0], c_r[1], CSV_data, flags=re.MULTILINE)

table_rows = CSV_data.split('\n')
while '' in table_rows: table_rows.remove('') # remove any empty rows

# double-check that source data format hasn't changed
row0 = table_rows[0]
row0_cells = row0.split('","')
for i, c in enumerate(row0_cells):
	row0_cells[i] = c.replace('"','') # discard remaining double quotes
expected_headers = { # at pythonic indices
	0: "Entity ID",
	1: "Work",
	2: "Author ID (person)",
	3: "Author (person)",
	4: "Attributed author ID (person)",
	5: "Attributed author (person)",
	23: "Commentary on ID (work)",
	24: "Commentary on (work)",
}
headers_found = [ row0_cells[i] for i in expected_headers.keys() ]
if headers_found != list(expected_headers.values()):
	print("warning, data format may have changed")
	input("press enter to continue")

# create and populate objects for Works and Authors

Entities = {} # cumulative lookup table by entity id

for row in table_rows[1:]: # skip column labels

	# split for simple list of row content, but adjust for extra quotes
	row_cells = row.split('","')
	for i, c in enumerate(row_cells):
		row_cells[i] = c.replace('"','') # discard remaining double quotes

	work_id = row_cells[0]
	if work_id in Entities:
		W = Entities[work_id]
	else:
		W = Work(work_id) # initialize with id
		Entities[work_id] = W

	# most names are a simple letter string, possibly with spaces or hyphens
	# but some exceptions (23) with commas, etc. are known =
	# this will look gross in the visualization
	# but it is a data problem, so I take no evasive action here
	W.name = row_cells[1]

	# manage potentially multiple authors
	# treat any available authorship equally (for now)

	author_ids = row_cells[2].split(', ') or row_cells[4].split(', ')
	while '' in author_ids: author_ids.remove('')
	author_names = row_cells[3].split(', ') or row_cells[5].split(', ')
	while '' in author_names: author_names.remove('')

	for i, author_id in enumerate(author_ids):

		if author_id in Entities:
			A = Entities[author_id]
		else:
			A = Author(author_id) # initialize with id
			Entities[A.id] = A

		A.name = author_names[i]

		(W.author_ids).append(A.id)
		(A.work_ids).append(W.id)

	# repeat for potentially multiple base texts

	base_text_ids = row_cells[23].split(', ')
	while '' in base_text_ids: base_text_ids.remove('')
	base_text_names = row_cells[24].split(', ')
	while '' in base_text_names: base_text_names.remove('')

	for i, base_text_id in enumerate(base_text_ids):

		if base_text_id in Entities:
			BT = Entities[base_text_id]
		else:
			BT = Work(base_text_id) # initialize with id
			Entities[BT.id] = BT

		BT.name = base_text_names[i]

		W.base_text_ids.append(BT.id)
		BT.commentary_ids.append(W.id)

save_content_to_file(Entities)
