from pipeline.results import journal_with_most_drugs, drugs_ref_in_pubmed


def test_journal_with_most_drugs():
    graph = {
        "paracetamol": {"mentions": [{"journal": "rmc", "date": "2020-01-01"}]},
        "ibuprofen": {"mentions": [{"journal": "rmc", "date": "2020-02-01"}]},
        "aspirin": {"mentions": [{"journal": "lequipe", "date": "2020-03-01"}]}
    }
    assert journal_with_most_drugs(graph) == "rmc"


def test_drugs_ref_in_pubmed():
    graph = {
        "paracetamol": {"mentions": [
            {"journal": "lequipe", "date": "2020-01-01"},
            {"journal": "rmc", "date": "2020-01-02"}
        ]},
        "ibuprofen": {"mentions": [
            {"journal": "rmc", "date": "2020-02-01"}
        ]},
        "aspirin": {"mentions": [
            {"journal": "lequipe", "date": "2020-03-01"}
        ]},
        "ethanol": {"mentions": [
            {"journal": "nejm", "date": "2020-04-01"}
        ]}
    }
    pubmed_journals = {"lequipe", "rmc"}  # only these count
    related = drugs_ref_in_pubmed(graph, pubmed_journals, "paracetamol")
    assert related == {"ibuprofen", "aspirin"}