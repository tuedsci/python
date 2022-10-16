# DUPLICATED DATA

import pandas as pd
import numpy as np

# --------------------------------------------------
# DUPLICATED DATA
# --------------------------------------------------

# %% Init
df = pd.DataFrame({
    "c1": ["A", "A", "B", "B", "C", "B"],
    "c2": ["x", "y", "x", "y", "x", "x"],
    "c3": [1, 2, -3, 0, 4, 1]
})

# %% Check duplicates
print(df.duplicated("c1"))  # True for each duplicated row
print(df.duplicated("c1").any())  # True if at least one duplicated row

# %% Drop duplicates (single col)
print(df.drop_duplicates("c1"))  # Keep first
print(df.drop_duplicates("c1", keep="last"))  # Keep last
print(df.drop_duplicates("c1", keep=False))  # Drop all duplicates

# %% Drop duplicates (multiple cols)
print(df.drop_duplicates(["c1", "c2"]))
print(df.drop_duplicates(["c1", "c2"], keep=False))

# %% Drop duplicates by index
# Init
df = pd.DataFrame({
    "c1": np.arange(1, 6),
    "c2": np.arange(1, 6) * 10
}, index=["US", "US", "CA", "VI", "CA"])

print(df[~df.index.duplicated()])  # Keep first
print(df[~df.index.duplicated(keep="last")])  # Keep last
print(df[~df.index.duplicated(keep=False)])  # Drop all
