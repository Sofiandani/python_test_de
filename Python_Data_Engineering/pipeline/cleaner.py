import pandas as pd
import re

def remove_hex_sequences(val):
    if not isinstance(val, str):
        val = str(val)
    #Delete sequences \xHH
    cleaned = re.sub(r'\\x[0-9a-fA-F]{2}', '', val)
    #Remove invisible returns and spaces
    cleaned = re.sub(r'[\r\n\t]', '', cleaned)
    return cleaned.strip().lower()

def clean_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Cleans a text column from a DataFrame: str, strip, lower.
    """
    df[column] = df[column].astype(str).str.strip().str.lower().apply(remove_hex_sequences)
    return df

def drop_na_column(df: pd.DataFrame, column: str = 'id') -> pd.DataFrame:
    """
    Drop a column, if it is empty, isna, or its content = 'nan'
    """
    if not pd.api.types.is_datetime64_any_dtype(df[column]):
        df[column] = df[column].astype(str).str.strip()
        df = df[df[column].notna() & (df[column] != '') & (df[column].str.lower() != 'nan') & (df[column].str.lower() != 'none')]
    else:
        df = df[df[column].notna()]

    return df.reset_index(drop=True)

def try_parse_date_column(df: pd.DataFrame, column: str = 'date') -> pd.DataFrame:
    """
    Cleans and attempts to parse the date column of a DataFrame.
    Drop the column if there is a problem with the date.
    """

    def try_parse(val):
        try:
            return pd.to_datetime(val, dayfirst=True)
        except Exception:
            return val  # keep raw value if error

    df[column] = df[column].astype(str).str.strip().apply(try_parse)
    df[column] = pd.to_datetime(df[column], errors='coerce', dayfirst=True)
    df=drop_na_column(df,column)
    return df