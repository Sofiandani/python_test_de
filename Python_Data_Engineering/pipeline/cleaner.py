import pandas as pd
import re

def remove_hex_sequences(val):
    if not isinstance(val, str):
        val = str(val)
    # Supprimer les séquences \xHH
    cleaned = re.sub(r'\\x[0-9a-fA-F]{2}', '', val)
    # Supprimer aussi les retours chariot et espaces invisibles
    cleaned = re.sub(r'[\r\n\t]', '', cleaned)
    return cleaned.strip().lower()

def clean_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Nettoie une colonne texte d'un DataFrame : str, strip, lower.
    """
    df[column] = df[column].astype(str).str.strip().str.lower().apply(remove_hex_sequences)
    return df

def drop_na_column(df: pd.DataFrame, column: str = 'id') -> pd.DataFrame:
    """
    Drop une colonne, s'il celle ci est vide, isna, ou son contenu = 'nan'
    """
    if not pd.api.types.is_datetime64_any_dtype(df[column]):
        df[column] = df[column].astype(str).str.strip()
        df = df[df[column].notna() & (df[column] != '') & (df[column].str.lower() != 'nan')]
    else:
        df = df[df[column].notna()]

    return df.reset_index(drop=True)

def try_parse_date_column(df: pd.DataFrame, column: str = 'date') -> pd.DataFrame:
    """
    Nettoie et tente de parser la colonne de date d'un DataFrame.
    Drop la colonne, s'il y a un problème avec la date
    """

    def try_parse(val):
        try:
            return pd.to_datetime(val, dayfirst=True)
        except Exception:
            return val  # garde la valeur brute si erreur

    df[column] = df[column].astype(str).str.strip().apply(try_parse)
    df[column] = pd.to_datetime(df[column], errors='coerce', dayfirst=True)
    df=drop_na_column(df,column)
    return df