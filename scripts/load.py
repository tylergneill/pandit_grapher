from datetime import datetime
import json
import os

from data_models import Entity
from util import time_execution

current_file_dir = os.path.dirname(os.path.abspath(__file__))
relative_data_dir = "../data"

@time_execution
def load_entities():
    input_filename = "2024-12-23-entities.json"
    input_json_path = os.path.join(current_file_dir, relative_data_dir, input_filename)
    with open(input_json_path, "r") as jsonfile:
        data = json.load(jsonfile)
    entities_by_id = {eid: Entity.from_dict(edict) for eid, edict in data.items()}
    return entities_by_id
