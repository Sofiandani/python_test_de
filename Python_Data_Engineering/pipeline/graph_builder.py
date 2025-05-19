from collections import defaultdict
from typing import List, Dict

def build_graph(mentions: List[Dict]) -> Dict:
    """
    Builds a graph of mentions by drug, with mention information by journal and mention date.
    """
    graph = defaultdict(lambda: {"mentions": []})

    for mention in mentions:
        drug = mention["drug"]
        journal = mention["journal"]
        date = mention["date"]

        graph[drug]["mentions"].append({
            "journal": journal,
            "date": date
        })

    return dict(graph)