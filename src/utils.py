import json
from pathlib import Path

LIBRARY_FILE = Path("../data/library.json")
WISHLIST_FILE = Path("../data/wishlist.json")


def load_data(file: Path):
    if not file.exists():
        return []

    data = json.loads(file.read_text())
    if isinstance(data, list):
        return data
    else:
        return []


def save_data(file: Path, data):
    file.write_text(json.dumps(data, indent=4))
