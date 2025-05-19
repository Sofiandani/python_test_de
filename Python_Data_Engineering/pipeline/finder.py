from typing import List, Dict
import pandas as pd

def find_mentions(df: pd.DataFrame, column: str, drugs: List[str]) -> List[Dict]:
    """
    Searches for drug mentions in a title column.
    Adds journal information and the date when the drug was mentioned.
    """
    mentions = []

    for _, row in df.iterrows():
        title = row[column]
        journal = row['journal']
        date = row['date']

        for drug in drugs:
            if drug in title:
                mentions.append({
                    "drug": drug,
                    "journal": journal,
                    "date": date if isinstance(date, str) else str(date)
                })

    return mentions