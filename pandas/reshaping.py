# DATA RESHAPING

import numpy as np
import pandas as pd
from pydataset import data

# --------------------------------------------------
# PIVOT
# --------------------------------------------------
# Convert from LONG format to WIDE format
# .pivot() is for simple use without aggregation
# Thus, it cannot be used when the index is duplicated
# For duplicated index, use .pivot_table()

# %% Init
long_df = pd.DataFrame({
    "year": sorted([2020, 2021, 2022] * 3),
    "country": ["US", "CA", "VN"] * 3,
    "value": range(1, 10)
})

# %% Year goes into index
# country goes into columns
# value goes into cells
pivoted = long_df.pivot(index="year", columns="country", values="value")
print(pivoted)  # Pivoted result
print(pivoted.loc[2020])  # Get data for 2020

# %% Similar to the above, but year goes to a separate column
pivoted = long_df.pivot(index="year", columns="country", values="value") \
    .reset_index()
print(pivoted)

# --------------------------------------------------
# PIVOT TABLES
# --------------------------------------------------

# %% Init
long_df_dup = pd.DataFrame({
    "year": sorted([2020, 2021, 2022] * 6),
    "country": ["US", "US", "CA", "CA", "VN", "VN"] * 3,
    "value": range(1, 19)
})

# %% Year goes into index
# Country goes into columns
# Some aggregation on value goes into cell
# aggfunc can be any agg function such as min, max, mean, ...
long_df_dup.pivot_table(
    index="year",
    columns="country",
    values="value",
    aggfunc="min"
)

# --------------------------------------------------
# MELT
# --------------------------------------------------
# Convert from WIDE format to LONG format

# %% Init
wide_df = pd.DataFrame({
    "first": ["Tue", "John", "Maria", "Jack"],
    "last": ["Nguyen", "Doe", "Smith", "Sparrow"],
    "height": [1.83, 1.92, 1.75, 1.71],
    "weight": [70, 82, 55, 67]
})

print(wide_df)

# %% Gather height and weight
# Two new column will be auto-created with names 'variable' and 'value'
wide_df.melt(id_vars=["first", "last"])

# %% Melt with custom name
wide_df.melt(
    id_vars=["first", "last"],
    var_name="measure",
    value_name="measurement"
)

# --------------------------------------------------
# STACK & UNSTACK
# --------------------------------------------------
# Stack a contingency table

# %% Init
df = pd.DataFrame([[1, 2], [3, 4]], index=["A", "B"], columns=["x", 'y'])
print(df)

# %% Stack
stacked = df.stack()
print(stacked)
print(stacked.at[("A", "x")])  # Scalar index the stacked result

stacked.unstack()

# %% Unstack (undo stack)
print(stacked.unstack())

# --------------------------------------------------
# CROSS TABULATION
# --------------------------------------------------

# %% Init
df = data("SLID")
print(df)

# %% Cross tab
s1 = df["language"]
s2 = df["sex"]
pd.crosstab(s1, s2)  # Absolute count (already dropped NA)
pd.crosstab(s1, s2, dropna=False)  # Better for counting
pd.crosstab(s1, s2, normalize="all")  # All cells sum to 1
pd.crosstab(s1, s2, normalize="index")  # Each row sums to 1
pd.crosstab(s1, s2, normalize="columns")  # Each col sums  to 1

# %% Cross tab with additional variables
pd.crosstab(s1, s2, values=df["age"], aggfunc="mean")  # Mean age
pd.crosstab(s1, s2, values=df["wages"], aggfunc=np.median)  # Median wages

# %% Add margins
pd.crosstab(s1, s2, normalize="all", margins=True)

# --------------------------------------------------
# EXPLODE A LIST-LIKE COLUMN
# --------------------------------------------------

# %% Init
df = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "addr": [["US"], ["US", "UK"], ["VN", "CA", "IT"], []]
})

print(df)

# %% Explode a series (empty list will produce NaN)
df["addr"].explode()

# %% Explode a column of a DF
df.explode("addr")

# %% Typical use cases
df = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "addr": ["US", "US|UK", "VN|CA|IT", ""]
})

df.assign(addr=df["addr"].str.split("|")).explode("addr")
