import pandas as pd
from pipeline.loader import load_csv, load_json
from pipeline.cleaner import try_parse_date_column, drop_na_column, clean_column
from pipeline.finder import find_mentions
from pipeline.graph_builder import build_graph
from pipeline.output import write_json
from pipeline.results import journal_with_most_drugs, drugs_ref_in_pubmed


def main():
    #Chargement des données
    drugs = load_csv('data/drugs.csv')
    pubmed_csv = load_csv('data/pubmed.csv')
    pubmed_json = load_json('data/pubmed.json')  
    clinical_trials = load_csv('data/clinical_trials.csv')

    # Fusion des fichiers pubmed csv et json
    pubmed = pd.concat([pubmed_csv, pubmed_json], ignore_index=True)

    # Nettoyage de la donnée
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

    # Correspondace entre médicament et titre
    drug_names = drugs['drug'].tolist()
    mentions_pubmed = find_mentions(pubmed, column='title', drugs=drug_names)
    mentions_clinical_trials= find_mentions(clinical_trials, column='scientific_title', drugs=drug_names)

    all_mentions = mentions_pubmed + mentions_clinical_trials

    # Construction du graphe
    drug_mentions_graph = build_graph(all_mentions)

    # Création du fichier JSON de sortie
    write_json(drug_mentions_graph, 'output/drug_mentions_graph.json')
    print("Pipeline terminée. Résultat : output/drug_mentions_graph.json")

    # BONUS
    # Journal avec le plus de médicaments différents
    print("Journal avec le plus de médicaments différents :", journal_with_most_drugs(drug_mentions_graph))

    # Médicament(s) mentionné par un même journal
    pubmed_journals = set(pubmed['journal'].unique())
    drug = 'ethanol'
    ref = drugs_ref_in_pubmed(drug_mentions_graph, pubmed_journals, drug)
    print(f"Médicament(s) liés à {drug} (pubmed)):", ref)

if __name__ == "__main__":
    main()