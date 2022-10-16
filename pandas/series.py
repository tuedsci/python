# PANDAS SERIES

import pandas as pd
import numpy as np

# --------------------------------------------------
# CREATE A SERIES
# --------------------------------------------------

# %% From a sequence
s = pd.Series([1, 2, 3, 4, 5])
print(s)

# %% Custom index
s = pd.Series([1, 2, 3, 4, 5], index=list("ABCDE"))
print(s)

# %% From a dict
s = pd.Series({"python": 1, "java": 2, "c++": 3})
print(s)

# --------------------------------------------------
# DTYPE PROMOTION
# --------------------------------------------------

# %% Int is promoted to float
s = pd.Series([1, 2, 1.5, 3.14])
print(s)

# %% But bool will NOT be promoted to int
s = pd.Series([True, False, 1, 2])
print(s)

# %% We can provide dtype argument to enforce type conversion
s = pd.Series([True, False, 1, 2], dtype=int)
print(s)

# %% Similarly, numbers are not promoted to string as in Numpy
s = pd.Series([1, 2, 1.5, "A"])
print(s)

# %% We have to specify dtype=str for explicit dtype promotion
s = pd.Series([1, 2, 1.5, "A"], dtype=str)
print(s)
print(type(s.iloc[0]))

# --------------------------------------------------
# ATTRIBUTES
# --------------------------------------------------
# %% Init
s = pd.Series([1, 2, 3, 4, 5])
print(s)

type(s.iloc[0])

# %% Common attributes
print(s.size)  # Num elements
print(s.dtype)  # Dtype of elements
print(s.index)  # Index
print(s.values)  # Values as a Numpy array
print(s.T)  # Transpose (itself, so not useful)
print(s.flags)  # Flags associated with s
print(s.hasnans)  # True if there is any NaN

# --------------------------------------------------
# SELECTION BY LOCATION (.iloc[])
# --------------------------------------------------
# Selection refers to indexing, slicing, and filtering
# Location-based selection of series is very similar to that of sequences

# %% Init
s = pd.Series([1, 2, 3, 4, 5], index=list("ABCDE"))
print(s)

# %% Index elements by position
print(s.iloc[0])  # First
print(s.iloc[2])  # Third
print(s.iloc[-1])  # Last

# %% Slice elements by position
print(s.iloc[:3])  # First 3
print(s.iloc[-3:])  # Last 3
print(s.iloc[2:])  # All except first 2
print(s.iloc[:-2])  # All except last 2

# --------------------------------------------------
# SELECTION BY LABEL (.loc[])
# --------------------------------------------------
# This selection method can be used with label indices or Boolean arrays

# %% Init
s = pd.Series([1, 2, 3, 4, np.nan, 5], index=list("ABCDEF"))
print(s)

# %% Index by label
print(s.loc["A"])  # Element with index label 'A'
print(s.loc["E"])  # Element with index label 'E'

# %% Slice by label
print(s.loc["A":"C"])  # Elements with indexes from 'A' to 'C' (inclusive)
print(s.loc["C":"A"])  # Empty

# %% Filter with a Boolean array (NaNs are treated as False)
print(s.loc[s >= 3])

# --------------------------------------------------
# VERSATILE INDEXER ([], NOT RECOMMENDED)
# --------------------------------------------------

# %% The following 2 statements are the same
print(s[0])
print(s["A"])

# %% However, I recommend explicitly using .iloc for selection by position
# and .loc for selection by label
print(s.iloc[0])
print(s.loc["A"])

# --------------------------------------------------
# SCALAR INDEXING (.iat[] / .at[])
# --------------------------------------------------

# %% Init
s = pd.Series({
    "US": 100,
    "CA": 200,
    "VI": 300
})

# %% Use .iat[] to get a scalar value by position
print(s.iat[0])  # First
print(s.iat[-1])  # Last

# %% Use .at to get a scalar value by label
print(s.at["VI"])  # VI
print(s.at["CA"])  # CA

# --------------------------------------------------
# BOOLEAN INDEXING
# --------------------------------------------------

# %% Init
s = pd.Series([1, 2, -3, 7, 4, np.nan, 10, -2.5])

# %% Single condition
print(s[s > 0])  # Positive
print(s[~(s > 0)])  # Not positive (non-positive and NaNs)
print(s[s.notnull()])  # Non NaNs

# %% Multiple conditions
print(s[(s >= 0) & (s <= 10)])
print(s[(s < 0) | (s > 5)])

# --------------------------------------------------
# OTHER SELECTION METHODS
# --------------------------------------------------

# %% Init
s = pd.Series([1, -2, 3, -3, 5, 7])
print(s)

# %% .isin()
print(s[s.isin(["CA", "VI"])])

# %% .where(cond, otherwise, inplace=False)
# This makes sure output has the same shape as s
print(s.where(s > 0))  # Non-positive value will become NaNs
print(s.where(s > 0, -s))  # Equivalent to s.abs()

# %% Selection and overwriting
s[s < 0] = 0  # Replace negatives with zeroes
print(s)

# --------------------------------------------------
# SUMMARY STATS
# --------------------------------------------------

# %% Init
s = pd.Series([1, 2, -3, 4])
print(s)

# %% Basic summary stats
print(s.min())  # Min: -3
print(s.max())  # Max: 4
print(s.mean())  # Mean / average: 1.
print(s.median())  # Median: 1.5
print(s.describe())  # All common summaries
