import json

def write_json(data: dict, path: str):
    """
    Writes a Python dictionary in JSON format, with readable indentation.
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
