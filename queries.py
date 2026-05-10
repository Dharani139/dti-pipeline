import sqlite3

DB_PATH = "dti_database.db"

def run_query(title, query):
    conn = sqlite3.connect(DB_PATH)
    print(f"\n--- {title} ---")
    rows = conn.execute(query).fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No results")
    conn.close()

if __name__ == "__main__":

    run_query(
        "Top 10 activities with lowest IC50 values",
        """
        SELECT molecule_id, target_id, value, units
        FROM activities
        ORDER BY value ASC
        LIMIT 10
        """
    )

    run_query(
        "How many drugs target each organism",
        """
        SELECT t.organism, COUNT(DISTINCT a.molecule_id) as drug_count
        FROM activities a
        JOIN targets t ON a.target_id = t.chembl_id
        GROUP BY t.organism
        ORDER BY drug_count DESC
        """
    )

    run_query(
        "Molecules approved after 2000",
        """
        SELECT name, approval_year, max_phase
        FROM molecules
        WHERE approval_year > '2000'
        ORDER BY approval_year DESC
        LIMIT 10
        """
    )

    run_query(
        "Average IC50 value across all activities",
        """
        SELECT ROUND(AVG(value), 2) as avg_ic50, 
               ROUND(MIN(value), 2) as min_ic50,
               ROUND(MAX(value), 2) as max_ic50
        FROM activities
        """
    )