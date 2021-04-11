from flask import (
    json,
    current_app as app
)
import json
import os


# Adds data to the list (of users or events)
# Doesn't update existing items
def commit_data_to_key(source_file: str, requested_key: str, data: dict):
    database = get_json_file(source_file)

    database[requested_key].append(data)

    save_json_file(source_file, database)


# Finds an item in a list (of users or events)
# Updates that item with the given data
def commit_data_with_id(source_file: str, requested_key: str, requested_id: int, data: dict):
    database = get_json_file(source_file)

    item = next((x for x in database[requested_key] if x["id"] == requested_id), None)

    if item is not None:
        item.update(data)

    save_json_file(source_file, database)


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
