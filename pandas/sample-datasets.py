# SAMPLE DATASETS FOR LEARNING PYTHON
import os
from pydataset import data

# %% View all available datasets
data()

# %% Load some sample datasets
data("AirPassengers")
data("Heating")

# %% Generate a preview for all sample dataset into a Markdown document
filename = "sample_datasets_preview.md"
if os.path.exists(filename):
    os.remove(filename)

with open(filename, "a") as f:
    f.write("# Sample dataset preview")
    f.write("\nGenerated by Tue Nguyen")

    for i, dset_meta in data().iterrows():
        # Extract dataset
        dset = data(dset_meta.dataset_id)

        # Write dataset name and description
        f.write(f"\n\n## {i + 1}. {dset_meta.dataset_id}\n")
        f.write(f"\n- Description: {dset_meta.title}")
        f.write(f"\n- Shape: {dset.shape}")

        # Convert to Markdown table
        # Extract first 2 rows
        head = dset.head(2)

        # Write header
        header = f"\n\n|{'|'.join(head.columns)}|"
        f.write(header)

        # Write header separator
        header_sep = f"\n|{'|'.join(['---'] * len(head.columns))}|"
        f.write(header_sep)

        # Write dtypes
        dtypes = f"\n|{'|'.join(dset.dtypes.values.astype(str))}|"
        f.write(dtypes)

        # Write 3 rows
        for _, row in head.iterrows():
            tbl_row = f"\n|{'|'.join(row.values.astype(str))}|"
            f.write(tbl_row)