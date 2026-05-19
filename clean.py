"""
Reads data/raw/events.csv, drops rows that have any missing fields,
an invalid event_type, or a non-positive duration_seconds, and
normalizes timestamp to ISO 8601 (that is, to the format YYYY-MM-DDTHH:MM:SS).
"""

import sys
import pandas as pd
from pathlib import Path

# Reads data/raw/events.csv
raw_path, out_path = sys.argv[1], sys.argv[2]

df = pd.read_csv(raw_path)

# Drop rows with any missing fields, invalid event types, or non-positive duration seconds
df = df.dropna(how="any")

valid_event_types = ["click", "login", "purchase", "scroll", "view"]
df = df[df["event_type"].isin(valid_event_types)]

# Keep only positive duration seconds (int)
df.loc[:, "duration_seconds"] = df["duration_seconds"].astype(int)
df = df[df["duration_seconds"] > 0]

# Normalize timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"], format='mixed')
df.loc[:, "timestamp"] = df["timestamp"].apply(lambda x: x.isoformat())

# export as file
Path(out_path).parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out_path, index=False)
