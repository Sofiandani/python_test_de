import json

def write_json(data: dict, path: str):
    """
    Écrit un dictionnaire Python au format JSON, avec indentation lisible.
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
