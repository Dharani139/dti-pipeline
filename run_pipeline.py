import subprocess
import sys

steps = [
    ("Fetching data from ChEMBL API...", "fetch.py"),
    ("Cleaning and loading into database...", "load.py"),
    ("Logging provenance...", "provenance.py"),
    ("Running queries...", "queries.py"),
]

if __name__ == "__main__":
    print("Starting DTI pipeline...\n")
    for message, script in steps:
        print(f">> {message}")
        result = subprocess.run([sys.executable, script])
        if result.returncode != 0:
            print(f"Pipeline failed at {script}. Stopping.")
            sys.exit(1)
        print()
    print("Pipeline completed successfully!")