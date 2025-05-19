from pipeline.graph_builder import build_graph


def test_build_graph_structure():
    mentions = [
        {"drug": "paracetamol", "journal": "lequipe", "date": "2020-01-01"},
        {"drug": "paracetamol", "journal": "rmc", "date": "2020-01-15"},
        {"drug": "ibuprofen", "journal": "rmc", "date": "2020-02-01"}
    ]

    graph = build_graph(mentions)

    assert "paracetamol" in graph
    assert len(graph["paracetamol"]["mentions"]) == 2
    assert graph["paracetamol"]["mentions"][0]["journal"] == "lequipe"
    assert "ibuprofen" in graph
    assert graph["ibuprofen"]["mentions"][0]["journal"] == "rmc"