import pandas as pd
from pipeline.loader import load_csv, load_json
from pipeline.cleaner import try_parse_date_column, drop_na_column, clean_column
from pipeline.finder import find_mentions
from pipeline.graph_builder import build_graph
from pipeline.output import write_json
from pipeline.results import journal_with_most_drugs, drugs_ref_in_pubmed


def main():
    # Loading data
    drugs = load_csv('data/drugs.csv')
    pubmed_csv = load_csv('data/pubmed.csv')
    pubmed_json = load_json('data/pubmed.json')  
    clinical_trials = load_csv('data/clinical_trials.csv')

    # Merging pubmed csv and json files
    pubmed = pd.concat([pubmed_csv, pubmed_json], ignore_index=True)

    # Data cleaning
    drugs = drop_na_column(drugs, 'atccode')
    drugs = clean_column(drugs, 'drug')

    pubmed = drop_na_column(pubmed_csv, 'id')
    pubmed = try_parse_date_column(pubmed_csv, 'date')
    pubmed = clean_column(pubmed, column='title')
    pubmed = clean_column(pubmed, column='journal')

    clinical_trials = drop_na_column(clinical_trials, 'id')
    clinical_trials = try_parse_date_column(clinical_trials, 'date')
    clinical_trials = clean_column(clinical_trials, column='scientific_title')
    clinical_trials = clean_column(clinical_trials, column='journal')

    # Correspondence between drug and title
    drug_names = drugs['drug'].tolist()
    mentions_pubmed = find_mentions(pubmed, column='title', drugs=drug_names)
    mentions_clinical_trials= find_mentions(clinical_trials, column='scientific_title', drugs=drug_names)

    all_mentions = mentions_pubmed + mentions_clinical_trials

    # Graph construction
    drug_mentions_graph = build_graph(all_mentions)

    # Creating the output JSON file
    write_json(drug_mentions_graph, 'output/drug_mentions_graph.json')
    print("Pipeline finished. Résultat : output/drug_mentions_graph.json")

    # BONUS
    # Journal with the most different medications
    print("Journal with the most different medications :", journal_with_most_drugs(drug_mentions_graph))

    # Drug(s) mentioned by the same journal
    pubmed_journals = set(pubmed['journal'].unique())
    drug = 'ethanol'
    ref = drugs_ref_in_pubmed(drug_mentions_graph, pubmed_journals, drug)
    print(f"Drug(s) related to {drug} (pubmed)):", ref)


if __name__ == "__main__":
    main()