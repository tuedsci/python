# DATA MERGING AND JOINING
# TODO:
#   - merge_asof(): approximate matching
import pandas as pd

# %% Init

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "age": [20, 25, 31]
})

df2 = pd.DataFrame({
    "id": [4, 5, 6],
    "age": [28, 22, 40]
})

df3 = pd.DataFrame({
    "id": [1, 1, 2, 4],
    "addr": ["US", "UK", "IT", "CA"]
})

df4 = pd.DataFrame({
    "edu": ["BSc", "MSc", "PhD"]
})

# --------------------------------------------------
# CONCAT
# --------------------------------------------------

# %% Concat vertically (top-bottom)
pd.concat([df1, df2], ignore_index=True)

# %% Concat horizontally (side by side)
pd.concat([df1, df4], axis=1)

# --------------------------------------------------
# MERGE (SIMILAR TO SQL JOINS)
# --------------------------------------------------

# %% Inner join
df1.merge(df3, on="id")

# %% Left join
df1.merge(df3, on="id", how="left")

# %% Right join
df1.merge(df3, on="id", how="right")

# %% Full join
df1.merge(df3, on="id", how="outer")

# %% Cross join
df1.join(df4, how="cross")

# --------------------------------------------------
# CHECK FOR DUPLICATE KEYS
# --------------------------------------------------
# Key uniqueness is checked BEFORE merge operations
# If violated, a MergeError exception will be raised

# %% Validate one-to-one
df1.merge(df3, on="id", validate="one_to_one")  # MergeError

# %% Validate one-to-many
df1.merge(df3, on="id", validate="one_to_many")  # OK

# --------------------------------------------------
# MERGE INDICATORS
# --------------------------------------------------
# Should be used with outer joins only
# - 'left_only': this key only appears on the left
# - 'right_only': this key only appears on the right
# - 'both': this key only appears on both sides

df1.merge(df3, on="id", how="outer", indicator=True)

# --------------------------------------------------
# JOIN ON INDEX
# --------------------------------------------------

# %% Init
left = pd.DataFrame({
    "A": ["A0", "A1", "A2"],
    "B": ["B0", "B1", "B2"]
}, index=["K0", "K1", "K2"])

right = pd.DataFrame({
    "C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]
}, index=["K0", "K2", "K3"])

# %% Left join index (default)
left.join(right)

# %% Inner join index
left.join(right, how="inner")

# %% Right join index
left.join(right, how="right")

# %% Full join index
left.join(right, how="outer")
