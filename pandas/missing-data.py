# MISSING DATA
# Starting from v1.0, Pandas is experimenting a native NA value
# to denote missing data instead of the traditional np.nan

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# OLD WAY OF REPRESENTING NA
# --------------------------------------------------

# %% Missing values are represented by np.nan by default
# Since nan is float, every element is promoted to float
s = pd.Series([1, 2, 3, None, np.nan])
print(s)
print(s.dtype)  # float64
print(type(s.iat[0]))  # numpy.float64
print(type(s.iat[-1]))  # numpy.float64
print(type(s.iat[-2]))  # numpy.float64

# --------------------------------------------------
# NEW WAY OF REPRESENTING NA
# --------------------------------------------------

# %% Pandas introduces pd.NA to represent null value to
# avoid type promotion
print(pd.NA)  # <NA>
print(type(pd.NA))  # pandas._libs.missing.NAType

# %% Operations involving NA usually producing NA
print(pd.NA + 1)
print(pd.NA * 3)
print(pd.NA == 42)

# %% For logical operations, pd.NA follows the rule of three-valued logic
# Read more: https://en.wikipedia.org/wiki/Three-valued_logic
print(True | pd.NA)  # True
print(False | pd.NA)  # NA
print(True & pd.NA)  # NA
print(False & pd.NA)  # False

# --------------------------------------------------
# SERIES CONTAINING NA
# --------------------------------------------------

# %% Nullable integer series
# We can set dtype="Int64" or dtype=pd.Int64Dtype()
s = pd.Series([1, 2, None, np.nan], dtype="Int64")
print(s)
print(s.dtype)  # Int64
print(type(s.iat[0]))  # numpy.int64
print(type(s.iat[-1]))  # pandas._libs.missing.NAType
print(type(s.iat[-2]))  # pandas._libs.missing.NAType

# %% Nullable float series
# We can set dtype="Int64" or dtype=pd.Int64Dtype()
s = pd.Series([1, 2, None, np.nan], dtype="Float64")
print(s)
print(s.dtype)  # Int64
print(type(s.iat[0]))  # numpy.float64
print(type(s.iat[-1]))  # pandas._libs.missing.NAType
print(type(s.iat[-2]))  # pandas._libs.missing.NAType

# Nullable string series
# %% We can set dtype="string" or dtype=pd.StringDtype()
s = pd.Series([1, 2, None, np.nan], dtype="string")
print(s.dtype)  # string
print(type(s.iat[0]))  # str
print(type(s.iat[-1]))  # pandas._libs.missing.NAType
print(type(s.iat[-2]))  # pandas._libs.missing.NAType

# Nullable datetime series
# %% We can set dtype="string" or dtype=pd.StringDtype()
pass

# --------------------------------------------------
# INSERT NULL VALUES
# --------------------------------------------------

# %% In old Pandas series, inserting None will result in np.nan
# and can cause type promotion
s = pd.Series([1, 2, 3])
print(s)  # int64
s.iat[0] = None
print(s)  # Become float64

# %% In new Pandas series, inserting None will result in np.NA
# and will not cause type promotion
s = pd.Series([1, 2, 3], dtype="Int64")
print(s)  # Int64
s.iloc[:2] = [None, np.nan]
print(s)  # Still Int64

# --------------------------------------------------
# CHECK NA
# --------------------------------------------------

# %% We can check NA using pd.isna() and pd.notna()
pd.isna(pd.NA)  # True
pd.isna(None)  # True
pd.isna(np.nan)  # True

pd.isna(42)  # False
pd.isna("")  # False
pd.isna([])  # array([], dtype=bool)
pd.isna([1, 2, None, np.nan])  # array([False, False,  True,  True])

# --------------------------------------------------
# FILL & DROP NA
# --------------------------------------------------

# %% Init
df = pd.DataFrame({
    "c1": [11, None, 31, None],
    "c2": [12, None, 32, None],
    "c3": [13, None, None, None]
}, dtype="Int64")

# %% Fill NA
print(df)
df.fillna(0)  # Fill all NaNs with 0
df.fillna(method="ffill")  # Forward fill, alternatively df.ffill()
df.fillna(method="bfill")  # Backward fill, alternatively df.bfill()
df.fillna(method="ffill", limit=1)  # Limit to fill 1 time
df.fillna({"c1": 100, "c2": 200})  # Custom fill by for each col

# %% Drop NA
print(df)
df.dropna()  # Drop a row if any cell has NA
df.dropna(how="any")  # Same as above
df.dropna(how="all")  # Drop a row if all cells have NaNs
df.dropna(subset=["c2", "c3"])  # Drop if any NA in c2 or c3
df.dropna(subset=["c2", "c3"], how="all")  # Drop if all NA in c2 or c3

# --------------------------------------------------
# INTERPOLATION
# --------------------------------------------------

# %% By default, .interpolate() does simple linear interpolation
s = pd.Series(np.random.uniform(1, 1.5, size=100))
s.iloc[10:20] = None  # Simulate missing value
print(s)
print(s.count())  # 90 non-null
print(s.interpolate().count())  # 100 non-null

# Disconnected plot
s.plot()
plt.show()

# Connected plot
s.interpolate().plot()
plt.show()

# %% But we can use fancy kinds of interpolations provided by scipy
# Note: scipy is required
s.interpolate(method="quadratic").plot()
plt.show()

# %% We can also set the limit for interpolation (just like with fill)
s.interpolate(limit=5).plot()
plt.show()

# --------------------------------------------------
# CASTING RULE
# --------------------------------------------------
# int -> float
# bool -> object
# float -> no cast
# object -> no cast
