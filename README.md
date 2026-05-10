# Drug-Target Interaction Pipeline

An ETL pipeline that collects, cleans, and stores drug-target interaction data from the ChEMBL biomedical database.

## What it does
- Fetches drug compounds, protein targets, and bioactivity data from the ChEMBL public API
- Cleans and normalizes the data using pandas
- Loads it into a structured SQLite database with three related tables
- Logs every pipeline run with timestamps and checksums for full data provenance

## Project Structure
- `fetch.py` — pulls raw data from ChEMBL API and saves to disk
- `clean.py` — normalizes and structures the raw data
- `load.py` — loads clean data into SQLite database
- `provenance.py` — logs each pipeline run for data lineage tracking

## How to run

```bash
# Install dependencies
pip install requests pandas

# Run the pipeline
python3 fetch.py
python3 load.py
python3 provenance.py
```

## Database Tables
- `molecules` — drug compounds with ChEMBL IDs and approval data
- `targets` — protein targets and their organisms
- `activities` — bioactivity measurements linking drugs to targets (IC50 values)
- `provenance` — pipeline run logs with timestamps and file checksums

## Data Source
[ChEMBL](https://www.ebi.ac.uk/chembl/) — a public biomedical database maintained by the European Bioinformatics Institute