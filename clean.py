"""
Reads data/raw/events.csv, drops rows that have any missing fields,
an invalid event_type, or a non-positive duration_seconds, and
normalizes timestamp to ISO 8601 (that is, to the format YYYY-MM-DDTHH:MM:SS).
"""

import sys
import pandas as pd

# Reads data/raw/events.csv
raw_path, out_path = sys.argv[1], sys.argv[2]

df = pd.read_csv(raw_path)

# Drop rows with any missing fields, invalid event types, or non-positive duration seconds
df = df.dropna(how="any")

valid_event_types = ["click", "login", "scroll", "view", "buy", "purchase"]
df = df[df["event_type"].isin(valid_event_types)]

df = df[df["duration_seconds"] > 0]

# Normalize timestamp
df.loc[:, "timestamp"] = pd.to_datetime(df["timestamp"], format='mixed')
df.loc[:, "timestamp"] = df["timestamp"].apply(lambda x: x.isoformat())

# export as file
df.to_csv(out_path, index=False)