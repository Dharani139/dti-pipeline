import pandas as pd
import json

def load_raw(filename):
    with open(f"raw/{filename}") as f:
        return json.load(f)

def clean_molecules(data):
    df = pd.DataFrame(data)
    df = df[["molecule_chembl_id", "pref_name", "molecule_type",
             "first_approval", "max_phase"]].copy()
    df.columns = ["chembl_id", "name", "type", "approval_year", "max_phase"]
    df = df.dropna(subset=["chembl_id"])
    df["name"] = df["name"].fillna("Unknown")
    return df

def clean_targets(data):
    df = pd.DataFrame(data)
    df = df[["target_chembl_id", "pref_name", "target_type", "organism"]].copy()
    df.columns = ["chembl_id", "name", "type", "organism"]
    df = df.dropna(subset=["chembl_id"])
    df["name"] = df["name"].fillna("Unknown")
    return df

def clean_activities(data):
    df = pd.DataFrame(data)
    df = df[["activity_id", "molecule_chembl_id", "target_chembl_id",
             "standard_type", "standard_value", "standard_units"]].copy()
    df.columns = ["activity_id", "molecule_id", "target_id",
                  "assay_type", "value", "units"]
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value", "molecule_id", "target_id"])
    return df

if __name__ == "__main__":
    molecules  = clean_molecules(load_raw("molecules.json"))
    targets    = clean_targets(load_raw("targets.json"))
    activities = clean_activities(load_raw("activities.json"))

    print(f"Molecules:  {len(molecules)} rows")
    print(f"Targets:    {len(targets)} rows")
    print(f"Activities: {len(activities)} rows")