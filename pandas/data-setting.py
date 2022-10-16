# DATA SETTING

import seaborn as sns
import numpy as np
import pandas as pd

# --------------------------------------------------
# SETTING DATA VALUES
# --------------------------------------------------

# %% Init
df = sns.load_dataset("dowjones")
print(df)

# %% Set a scalar value by location
df.iat[0, 1] = 0
print(df.head(2))

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
