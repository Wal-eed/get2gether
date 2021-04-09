import json
import os
from flask import (
    json,
    current_app as app
)

# TODO: implement all these database functions
# Pretty sure jsonify and json.load return dicts right?
# ¯\_(ツ)_/¯

# commit_data_to_key just stores the data into our json file
def commit_data_to_key(source_file: str, requested_key: str, data: dict) -> bool:
    database = get_json_file(source_file)

    # Not sure which way to update the dict
    # depends on how the function is called
    #
    # database[requested_key] = data
    # database.update(data)

    save_json_file(source_file, database)
    
    # Is this supposed to return something?


def get_json_file(source_file: str) -> dict:
    source_url = json_url(source_file)

    with open(source_url) as json_file:
        data = json.load(json_file)

    return data


def save_json_file(source_file: str, database: dict):
    source_url = json_url(source_file)

    with open(source_url, 'w') as json_file:
        json.dump(database, json_file)

def json_url(source_file: str) -> str:
    # app.root_path == backend/Get2Gether
    return os.path.join(app.root_path, "database", source_file + ".json")