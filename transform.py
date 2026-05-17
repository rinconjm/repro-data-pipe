"""
reads `data/clean/events.csv` and adds a `date` column containing the date portion of timestamp 
in `YYYY-MM-DD` format. Writes the result to data/transformed/events.csv.
"""

import sys
import pandas as pd

# Reads data/clean/events.csv
clean_path, out_path = sys.argv[1], sys.argv[2]

df = pd.read_csv(clean_path)

df['date'] = df["timestamp"].str[:10]

# Write result to data/transformed/events.csv
df.to_csv(out_path, index=False)