# SORTING DATA
import seaborn as sns

# --------------------------------------------------
# SORT VALUES
# --------------------------------------------------
# %% Init
df = sns.load_dataset("diamonds")
print(df)

# %% Sort by 1 column
print(df.sort_values("color"))  # ASC
print(df.sort_values("color", ascending=False))  # DESC

# %% Sort by multiple columns
print(df.sort_values(["cut", "color"]))
print(df.sort_values(["cut", "color"], ascending=False))
print(df.sort_values(["cut", "color"], ascending=[False, True]))

# --------------------------------------------------
# SORT INDEX
# --------------------------------------------------
