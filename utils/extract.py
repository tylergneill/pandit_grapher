# extract from big CSV to small CSV

import os
import pandas as pd

# Load the input CSV file

current_file_dir = os.path.dirname(os.path.abspath(__file__))
relative_data_dir = "../data"
input_filename = "2024-12-23-pandit-entities-export.csv"
df = pd.read_csv(
    os.path.join(current_file_dir, relative_data_dir, input_filename),
    dtype=str,
)

# Specify the desired columns
columns_to_keep = [
    "Content type",
    "ID",
    "Title",
    "Author (person IDs)",
    "Authors (person)",
    "Attributed author (person ID)",
    "Attributed author (person)",
    "Commentary on (work ID)",
    "Commentary on (work)"
]

# Filter the DataFrame to keep only the specified columns
df_filtered = df[columns_to_keep]

# Further filter: Only keep rows where "Content type" is "Work"
df_filtered = df_filtered[df_filtered["Content type"] == "Work"]

# Combine "Attributed author (person ID)" into "Author (person IDs)"
df_filtered["Author (person IDs)"] = df_filtered["Author (person IDs)"].fillna("").astype(str) + "; " + df_filtered["Attributed author (person ID)"].fillna("").astype(str)
df_filtered["Authors (person)"] = df_filtered["Authors (person)"].fillna("").astype(str) + "; " + df_filtered["Attributed author (person)"].fillna("").astype(str)

# Clean up double separators and trailing separators
df_filtered["Author (person IDs)"] = df_filtered["Author (person IDs)"].str.replace(r";\s*;", ";", regex=True).str.strip("; ")
df_filtered["Authors (person)"] = df_filtered["Authors (person)"].str.replace(r";\s*;", ";", regex=True).str.strip("; ")

# Drop the "Content type" and "Attributed author" columns
df_filtered = df_filtered.drop(columns=["Content type", "Attributed author (person ID)", "Attributed author (person)"], errors="ignore")

# Drop the "Content type" column
df_filtered = df_filtered.drop(columns=["Content type"], errors="ignore")

# Rename columns
df_filtered.rename(columns={
    "Author (person IDs)": "Authors (IDs)",
    "Authors (person)": "Authors (names)",
    "Commentary on (work ID)": "Base texts (IDs)",
    "Commentary on (work)": "Base texts (names)"
}, inplace=True)

# Replace NaN with empty strings to avoid 'nan' in output
df_filtered.fillna("", inplace=True)

# Save the output to a new CSV file
output_filename = "2024-12-23-works-raw.csv"
df_filtered.to_csv(os.path.join(current_file_dir, relative_data_dir, output_filename), index=False)

print(f"Filtered CSV saved as {output_filename}")
