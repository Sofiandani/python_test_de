import pandas as pd
import json
import re
import os

def auto_fix_json_file(path: str, fixed_path: str = None) -> bool:
    """
    Fix an invalid JSON file (eg trailing comma) only if necessary.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Apply corrections
        cleaned_content = re.sub(r',(\s*[\]\}])', r'\1', original_content)

        # If there is nothing to correct, we do not create an unnecessary file
        if original_content == cleaned_content:
            print(f"Aucun problème détecté. Le fichier est déjà valide : {path}")
            return True

        # Determine the exit path
        if not fixed_path:
            base, ext = os.path.splitext(path)
            fixed_path = f"{base}_fixed{ext}"

        with open(fixed_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        # Checking that the corrected file is valid JSON
        with open(fixed_path, 'r', encoding='utf-8') as f:
            json.load(f)

        print(f"Corrected and saved JSON file : {fixed_path}")
        return True

    except Exception as e:
        print(f"Automatic correction failed : {e}")
        return False



def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def load_json(path: str) -> pd.DataFrame:
    """
    Loads a JSON file into a DataFrame, with automatic correction if necessary.
    """
    # Correct if necessary and get the file to load
    base, ext = os.path.splitext(path)
    fixed_path = f"{base}_fixed{ext}"

    was_fixed = auto_fix_json_file(path, fixed_path)

    final_path = fixed_path if was_fixed else path

    # Reading the file (corrected or not)
    with open(final_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return pd.DataFrame(data)