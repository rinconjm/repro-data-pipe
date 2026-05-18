"""
features -- reads data/transformed/events.csv and adds two new columns to each row:
duration_minutes: the event's duration_seconds divided by 60.
weekday: the day-of-week name of the event's date, written in full (e.g., Monday, Tuesday, ..., Sunday).
"""

import sys
import pandas as pd
from pathlib import Path

in_path, out_path = sys.argv[1], sys.argv[2]

df = pd.read_csv(in_path)

df["duration_minutes"] = df["duration_seconds"] / 60

dt_date = pd.to_datetime(df["date"])
df["weekday"] = dt_date.dt.day_name()

# Write result to data/transformed/events.csv
Path(out_path).parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out_path, index=False)