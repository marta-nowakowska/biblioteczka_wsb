import json
import os

import json
import os

def load_data(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    return []

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

