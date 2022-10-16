# MISSING DATA
import pandas as pd
import numpy as np

# %% Init
data = [
    [np.nan, 2, np.nan, 0],
    [3, 4, np.nan, 1],
    [np.nan, np.nan, np.nan, np.nan],
    [np.nan, 3, np.nan, 4]
]
cols = ["c1", "c2", "c3", "c4"]
df = pd.DataFrame(data, columns=cols)

print(df)

# %% Check NaNs
print(df.isna())
print(df.isnull())

# %% Fill NaNs
df.fillna(0)  # Fill all NaNs with 0
df.fillna(method="ffill")  # Forward fill
df.fillna(method="bfill")  # Backward fill
df.fillna({"c1": 0, "c2": -1})  # Custom fill by for each col

# %% Drop NaNs
df.dropna()  # Drop a row if any cell has NaN
df.dropna(how="any")  # Same as above
df.dropna(how="all")  # Drop a row if all cells have NaNs
df.dropna(subset=["c1", "c2"])  # Drop if any NaNs in c1 or c2
df.dropna(subset=["c1", "c2"], how="all")  # Drop if all NaNs in c1 and c2
