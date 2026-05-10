import sqlite3
import pandas as pd
from clean import clean_molecules, clean_targets, clean_activities, load_raw

DB_PATH = "dti_database.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables(conn):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS molecules (
            chembl_id     TEXT PRIMARY KEY,
            name          TEXT,
            type          TEXT,
            approval_year TEXT,
            max_phase     REAL
        );

        CREATE TABLE IF NOT EXISTS targets (
            chembl_id TEXT PRIMARY KEY,
            name      TEXT,
            type      TEXT,
            organism  TEXT
        );

        CREATE TABLE IF NOT EXISTS activities (
            activity_id TEXT PRIMARY KEY,
            molecule_id TEXT REFERENCES molecules(chembl_id),
            target_id   TEXT REFERENCES targets(chembl_id),
            assay_type  TEXT,
            value       REAL,
            units       TEXT
        );
    """)
    conn.commit()

def load_df(conn, df, table_name):
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into '{table_name}'")

if __name__ == "__main__":
    molecules  = clean_molecules(load_raw("molecules.json"))
    targets    = clean_targets(load_raw("targets.json"))
    activities = clean_activities(load_raw("activities.json"))

    conn = get_connection()
    create_tables(conn)
    load_df(conn, molecules,  "molecules")
    load_df(conn, targets,    "targets")
    load_df(conn, activities, "activities")
    conn.close()
    print("Done. Database saved to dti_database.db")