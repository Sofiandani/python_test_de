import pandas as pd
from pipeline.finder import find_mentions

def test_find_mentions_detects_exact_drug():
    df = pd.DataFrame({
        'title': ['Paracetamol is effective', 'Ibuprofen vs placebo', 'No drug here'],
        'journal': ['Lancet', 'BMJ', 'NEJM'],
        'date': ['2020-01-01', '2020-01-02', '2020-01-03']
    })
    drugs = ['paracetamol', 'ibuprofen']
    df['title'] = df['title'].str.lower()
    mentions = find_mentions(df, column='title', drugs=drugs)
    assert len(mentions) == 2
    assert mentions[0]['drug'] == 'paracetamol'
    assert mentions[1]['drug'] == 'ibuprofen'

def test_find_mentions_returns_empty_list_if_no_match():
    df = pd.DataFrame({
        'title': ['random text', 'another one'],
        'journal': ['A', 'B'],
        'date': ['2020-01-01', '2020-01-02']
    })
    mentions = find_mentions(df, column='title', drugs=['aspirin'])
    assert mentions == []
