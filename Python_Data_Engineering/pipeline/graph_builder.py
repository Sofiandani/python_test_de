from collections import defaultdict
from typing import List, Dict

def build_graph(mentions: List[Dict]) -> Dict:
    """
    Construit un graphe de mentions par médicament, avec les infos de mention par journal et date de mention.
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