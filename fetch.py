import requests
import json
import os

BASE_URL = "https://www.ebi.ac.uk/chembl/api/data"

def fetch_molecules(limit=100):
    url = f"{BASE_URL}/molecule.json?limit={limit}&molecule_type=Small+molecule"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["molecules"]

def fetch_targets(limit=100):
    url = f"{BASE_URL}/target.json?limit={limit}&target_type=SINGLE+PROTEIN"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["targets"]

def fetch_activities(limit=200):
    url = f"{BASE_URL}/activity.json?limit={limit}&standard_type=IC50"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["activities"]

def save_raw(data, filename):
    os.makedirs("raw", exist_ok=True)
    with open(f"raw/{filename}", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data)} records to raw/{filename}")

if __name__ == "__main__":
    print("Fetching molecules...")
    molecules = fetch_molecules()
    save_raw(molecules, "molecules.json")

    print("Fetching targets...")
    targets = fetch_targets()
    save_raw(targets, "targets.json")

    print("Fetching activities...")
    activities = fetch_activities()
    save_raw(activities, "activities.json")

    print("Done fetching all data.")
