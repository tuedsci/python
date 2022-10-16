# DATA SELECTION
import seaborn as sns

# --------------------------------------------------
# SELECT COLUMNS
# --------------------------------------------------

# %% Init
df = sns.load_dataset("diamonds")
print(df)

# %% Select 1 column (get a series)
s = df["carat"]  # Get carat column
print(type(s))  # Series type

# %% Pick cols (potentially non-consecutive)
print(df[["carat", "cut", "clarity"]])  # Label-based pick cols
print(df.loc[:, ["carat", "cut", "clarity"]])  # Equivalent to the above
print(df.iloc[:, [0, 1, -1]])  # Location-based pick cols

# %% Slice cols (consecutive)
print(df.loc[:, "carat":"clarity"])  # Label-based slice cols
print(df.iloc[:, :4])  # Location-based slice cols

# --------------------------------------------------
# SELECT ROWS
# --------------------------------------------------

# %% Filter rows with Boolean indexing
print(df[df["cut"] == "Premium"])  # Equal
print(df[df["color"].isin(["E", "H"])])  # In
print(df[~df["color"].isin(["E", "H"])])  # Not in (potentially include NaNs)
print(df[df["carat"].between(0.2, 0.3, "both")])  # Between (both end included)

# %% Filter rows with .query (alternative version of Boolean indexing)
# .query uses numexpr, which is slightly faster than Boolean indexing
# for large data frames (>= 20k rows)
df.query("cut == 'Premium'")
df.query("color in ('E', 'H')")
df.query("color not in ('E', 'H')")
df.query("0.2 <= carat <= 0.3")

# %% Use .query with variable referencing
chosen_cuts = ["Very Good", "Premium"]
df.query("cut in @chosen_cuts")
