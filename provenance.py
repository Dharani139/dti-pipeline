import sqlite3
import hashlib
from datetime import datetime, timezone

DB_PATH = "dti_database.db"

def log_run(source, stage, row_count, file_path=None):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS provenance (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp  TEXT,
            source     TEXT,
            stage      TEXT,
            row_count  INTEGER,
            checksum   TEXT
        )
    """)

    checksum = None
    if file_path:
        with open(file_path, "rb") as f:
            checksum = hashlib.md5(f.read()).hexdigest()

    conn.execute("""
        INSERT INTO provenance (timestamp, source, stage, row_count, checksum)
        VALUES (?, ?, ?, ?, ?)
    """, (datetime.now(timezone.utc).isoformat(), source, stage, row_count, checksum))

    conn.commit()
    conn.close()
    print(f"[provenance] {stage} | {source} | {row_count} rows | checksum: {checksum}")

if __name__ == "__main__":
    log_run(
        source="ChEMBL API",
        stage="fetch",
        row_count=100,
        file_path="raw/molecules.json"
    )
    log_run(
        source="ChEMBL API",
        stage="fetch",
        row_count=100,
        file_path="raw/targets.json"
    )
    log_run(
        source="ChEMBL API",
        stage="fetch",
        row_count=195,
        file_path="raw/activities.json"
    )