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
