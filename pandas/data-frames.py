# PANDAS DATA FRAMES

import pandas as pd
import numpy as np

# --------------------------------------------------
# CREATE A DATA FRAME
# --------------------------------------------------

# %% From a dict of columns
data = {
    "name": ["Jack", "Maria", "Tom"],
    "age": [20, 25, 31],
    "edu": ["BSc", "MSc", "PhD"]
}

pd.DataFrame(data)

# %% From a sequence of rows
data = [
    ("Jack", 20, "BSc"),
    ("Maria", 25, "MSc"),
    ("Tom", 31, "PhD")
]

pd.DataFrame(data, columns=["name", "age", "edu"])

# --------------------------------------------------
# GET BASIC INFO
# --------------------------------------------------

# %% Init
data = {
    "name": ["Jack", "Maria", "Tom"],
    "age": [20, 25, 31],
    "edu": ["BSc", "MSc", "PhD"]
}

df = pd.DataFrame(data)

# %% Basic info
print(df.dtypes)  # Dtypes of columns
print(df.columns)  # Column names
print(df.shape)  # Num rows and cols
df.head(2)  # First 2 rows
df.tail(2)  # Last 2 rows
print(df.values)  # Numpy array representation
print(df.T)  # Transpose
