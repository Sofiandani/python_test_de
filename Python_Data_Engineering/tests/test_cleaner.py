import pandas as pd
from pipeline.cleaner import clean_column, drop_na_column, try_parse_date_column

def test_clean_column():
    df = pd.DataFrame({'col': [' Drug ', 'PARACETAMOL', ' ibuprofen\n']})
    cleaned = clean_column(df.copy(), 'col')
    assert cleaned['col'].tolist() == ['drug', 'paracetamol', 'ibuprofen']

def test_drop_na_column():
    df = pd.DataFrame({'id': ['1', '', None, 'nan', '2']})
    result = drop_na_column(df, 'id')
    assert result['id'].tolist() == ['1', '2']

def test_try_parse_date_column():
    df = pd.DataFrame({'date': ['01/01/2020', '2020-01-02', 'invalid']})
    parsed = try_parse_date_column(df.copy(), 'date')
    assert len(parsed) == 2