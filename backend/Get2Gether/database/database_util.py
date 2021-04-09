import os
from flask import (
    json,
    current_app as app
)

# TODO: implement all these database functions

# commit_data_to_key just stores the data into our json file
def commit_data_to_key(source_file: str, requested_key: str, data: json) -> bool:
    pass

def get_json_file(source_file: str) -> json:
    # app.instance_path == backend/Get2Gether
    source_url = os.path.join(app.instance_path, "database", source_file + ".json")

    with open(source_url) as json_file:
        data = json.load(json_file)

    return data