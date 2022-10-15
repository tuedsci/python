# PANDAS DATA FRAMES

# %% Imports
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

# --------------------------------------------------
# FILTERING ROWS
# --------------------------------------------------

# %% Init
df = pd.DataFrame({
    "name": ["A", "B", "A", "C", "D"],
    "score": [0.5, 2.7, 3, 4, 3.7],
    "credits": [3, 3, 2, 4, 3]
})

# %% Pure Python filtering
print(df[df["score"] >= 1])
print(df[(df["score"] >= 1) & (df["credits"] >= 3)])

# %% Filtering with .query
# Note: we can use English and/or instead of &/|
print(df.query("name == 'A'"))
print(df.query("name in ['A', 'B']"))
print(df.query("name not in ['A', 'B']"))
print(df.query("(score >= 1) & (credits >= 3)"))

# --------------------------------------------------
# SELECTION AND OVERWRITING
# --------------------------------------------------

# %% Init
df = pd.DataFrame({
    "id": range(1, 6),
    "score": [0.5, 2, 3.5, 3.7, 4]
})

# %% Binary conditions
df["is_passed"] = np.where(df["score"] >= 1, True, False)

# %% Multiple conditions (like SQL case when)
df.query("score > 1")

cond = [
    df["score"].between(0, 1, "left"),
    df["score"].between(1, 2, "left"),
    df["score"].between(2, 3, "left"),
    df["score"].between(3, 4, "left"),
    df["score"] == 4
]

choices = ["F", "D", "C", "B", "A"]
df["letter_grade"] = np.select(cond, choices)
