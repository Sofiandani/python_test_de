def journal_with_most_drugs(graph: dict) -> str:
    journal_drug_map = {}

    for drug, data in graph.items():
        for mention in data.get("mentions", []):
            journal = mention["journal"]
            journal_drug_map.setdefault(journal, set()).add(drug)

    return max(journal_drug_map.items(), key=lambda x: len(x[1]))[0]


def drugs_ref_in_pubmed(graph: dict, pubmed_journals: set, drug_name: str) -> set:
    if drug_name not in graph:
        return set()

    target_journals = {
        mention['journal'] for mention in graph[drug_name]["mentions"]
        if mention["journal"] in pubmed_journals
    }

    related = set()

    for other_drug, data in graph.items():
        if other_drug == drug_name:
            continue
        for mention in data["mentions"]:
            if mention["journal"] in target_journals:
                related.add(other_drug)

    return related
