import pandas as pd
import json
import re
import os

def auto_fix_json_file(path: str, fixed_path: str = None) -> bool:
    """
    Corrige un fichier JSON invalide (ex : virgule finale) seulement si nécessaire.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Appliquer les corrections
        cleaned_content = re.sub(r',(\s*[\]\}])', r'\1', original_content)

        # Si rien à corriger, on ne crée pas de fichier inutile
        if original_content == cleaned_content:
            print(f"Aucun problème détecté. Le fichier est déjà valide : {path}")
            return True

        # Déterminer le chemin de sortie
        if not fixed_path:
            base, ext = os.path.splitext(path)
            fixed_path = f"{base}_fixed{ext}"

        with open(fixed_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        # Vérification que le fichier corrigé est bien du JSON valide
        with open(fixed_path, 'r', encoding='utf-8') as f:
            json.load(f)

        print(f"Fichier JSON corrigé et sauvegardé : {fixed_path}")
        return True

    except Exception as e:
        print(f"Échec de la correction automatique : {e}")
        return False



def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def load_json(path: str) -> pd.DataFrame:
    """
    Charge un fichier JSON en DataFrame, avec correction automatique si nécessaire.
    """
    # Corrige si besoin et obtient le fichier à charger
    base, ext = os.path.splitext(path)
    fixed_path = f"{base}_fixed{ext}"

    was_fixed = auto_fix_json_file(path, fixed_path)

    final_path = fixed_path if was_fixed else path

    # Lecture du fichier (corrigé ou non)
    with open(final_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return pd.DataFrame(data)