from datetime import datetime
from functools import wraps
import json

SUPPRESS_TIME_DECORATOR = True  # Set this to True to suppress the decorator, False to enable it


def load_config_dict_from_json_file():
    settings_file_path = 'config.json'
    config_data = open(settings_file_path, 'r').read()
    config = json.loads(config_data)
    return config


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if SUPPRESS_TIME_DECORATOR:
            return func(*args, **kwargs)
        print(f"{func.__name__}", end=" ", flush=True)
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        duration = end - start
        duration_rounded = round(duration.total_seconds() * 1000) / 1000
        print(f"executed in {duration_rounded} seconds")
        return result
    return wrapper


def find_app_version():
    app_version_filepath = './VERSION'
    with open(app_version_filepath, 'r', encoding='utf8') as file:
        # Assuming the __app_version__ line is the first line
        return file.readline().strip().split('=')[1].strip().replace("'", "").replace('"', '')


def find_pandit_data_version():
    data_version_filepath = './VERSION'
    with open(data_version_filepath, 'r', encoding='utf8') as file:
        # Assuming the __pandit_data_version__ line is the second line
        return file.readlines()[1].strip().split('=')[1].strip().replace("'", "").replace('"', '')


def find_etext_data_version():
    data_version_filepath = './VERSION'
    with open(data_version_filepath, 'r', encoding='utf8') as file:
        # Assuming the __etext_data_version__ line is the third line
        return file.readlines()[2].strip().split('=')[1].strip().replace("'", "").replace('"', '')
