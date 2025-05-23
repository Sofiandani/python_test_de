# Drug Mentions Pipeline

This project is a modular Python data pipeline that detects mentions of drugs in scientific publications (from PubMed and Clinical Trials) and builds a JSON graph linking each drug to the journals and dates where it is mentioned.

---

# Features

- Load CSV and JSON data from PubMed and Clinical Trials
- Clean and normalize text, date and column values
- Detect drug mentions in publication titles
- Build a drug-to-journal graph with mention dates
- Export to JSON
- Bonus analysis: most-referencing journal, related drugs via PubMed

---

# Project Structure

├── main.py # Entry point for the pipeline

├── pipeline/

│ ├── loader.py # load_csv(), load_json()

│ ├── cleaner.py # clean_column(), drop_na_column(), try_parse_date_column()

│ ├── finder.py # find_mentions()

│ ├── graph_builder.py # build_graph()

│ ├── output.py # write_json()

│ └── results.py # journal_with_most_drugs(), drugs_ref_in_pubmed()

├── data/ # Raw input files (CSV/JSON)

├── output/ # Output folder for final JSON

├── tests/ # Unit tests (pytest)

├── requirements.txt # Python dependencies

└── README.md

# Setup & Dependencies
## Requirements

- Python 3.8+

### Virtual environment setup

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate it
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Deactivate the environment when done
deactivate
```


## Execute the main script
```bash
python main.py
```
 - Load and clean the data
 - Detect drug mentions in titles
 - Build the graph of mentions
 - Export the graph to output/drug_mentions_graph.json
 - Print answers to bonus business questions

## Final output
The final output is saved as:
```bash
output/drug_mentions_graph.json
```

# Tests

Unit tests are provided in the tests/ folder.
They validate the main components of the pipeline, including:

## What is tested
 - test_cleaner.py	Cleaning logic: date parsing, ID filtering, column normalization
 - test_finder.py	Drug mention detection in titles
 - test_graph_builder.py	Graph structure generation from mentions
 - test_results.py	Bonus analysis: most frequent journal, related drugs via PubMed

Run all tests with:
```bash
python -m pytest
```