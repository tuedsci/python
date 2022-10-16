# TEXT DATA
# References:
#   - https://pandas.pydata.org/docs/user_guide/text.html
import pandas as pd
import re

# --------------------------------------------------
# TEXT DATA TYPE
# --------------------------------------------------
# There are 2 ways to store text data in Pandas
# - object: Numpy array dtype
# - StringDtype: new in Pandas 1.0 (recommended)
# For backward compatibility, object dtype is still the default type
# when Pandas infer text data

# %% Text data with default object dtype
s = pd.Series(list("abcde"))
print(s)
print(s.dtype)

# %% Explicitly set dtype to StringDtype
s = pd.Series(list("abcde"), dtype="string")
print(s)
print(s.dtype)

# %% We can convert dtype object to string
s = pd.Series(list("abcde")).astype("string")
print(s.dtype)

# %% String dtype with NaN
s = pd.Series(["1", "2", None], dtype="string")
print(s)
print(s.dtype)  # string
print(type(s[0]))  # str
print(type(-1))  # int

# --------------------------------------------------
# INDEXING WITH .str[]
# --------------------------------------------------
# %% Init
s = pd.Series(
    ["Tue", "hoA", "timon123", "\tHahaha  ", None, "HELLO WORLD", 42],
    dtype="string"
)

print(s)

# --------------------------------------------------
# STRING METHODS
# --------------------------------------------------

# %% Init
s = pd.Series(
    ["Tue", "hoA", "timon123", "\tHahaha  ", None, "HELLO WORLD", 42, "\n\t"],
    dtype="string"
)

# %% Indexing
print(s)
print(s.str[0])  # First
print(s.str[3])  # Fourth
print(s.str[-1])  # Last
print(s.str[:3])  # First 3
print(s.str[-3:])  # Last 3

# %% Num chars
print(s.str.len())

# %% Case checking
print(s[s.str.isupper()])
print(s[s.str.islower()])
print(s[s.str.istitle()])
print(s[s.str.isalpha()])
print(s[s.str.isalnum()])
print(s[s.str.isdigit()])
print(s[s.str.isnumeric()])
print(s[s.str.isdecimal()])
print(s[s.str.isspace()])

# %% Case transformation
print(s.str.upper())
print(s.str.lower())
print(s.str.title())
print(s.str.capitalize())
print(s.str.swapcase())

# %% White space trimming
print(s.str.lstrip())
print(s.str.rstrip())
print(s.str.strip())

# %% Prefix and suffix removal
s = pd.Series(["lec_01_intro.txt", "lec_02_variables.txt", "exam_final.docx"])
print(s.str.removeprefix("lec_"))
print(s.str.removesuffix(".txt"))

# %% Splitting
# Note: use .str.rsplit() for right splitting
s = pd.Series(["a_b_c", "c_d_e", None, "f_g_h"], dtype="string")
print(s.str.split("_"))  # Split without expanding
print(s.str.split("_").str[0])  # First element
print(s.str.split("_").str[-1])  # Last element
print(s.str.split("_", expand=True))  # Split and expand all
print(s.str.split("_", expand=True, n=1))  # Split and expand to 2 cols
print(s.str.rsplit("_", expand=True, n=1))  # Same as above, but right split

# %% Partitioning
# Note: use .str.rpartition for right partitioning
s = pd.Series(["name: Tue", "edu: MSc", "country: VN"], dtype="string")
print(s)
print(s.str.partition(":"))  # Expand to 3 cols
print(s.str.partition(":", expand=False))  # No expansion
print(s.str.partition(":", expand=False).str[0])  # Get first part
print(s.str.partition(":", expand=False).str[-1])  # Get last part

# %% Joining
s = pd.Series([["CA", "Quebec"], ["VN", "Hai Phong"], ["IT", "Milano"]])
print(s)
print(s.str.join(", "))

# %% Concatenation
s = pd.Series(["Cat", "Dog", None, "Duck", "Tiger"], dtype="string")
print(s)
print(s.str.cat())  # CatDogDuckTiger
print(s.str.cat(sep="_"))  # Cat_Dog_Duck_Tiger
print(s.str.cat(sep="_", na_rep="?"))  # Include missing values
print(s.str.cat(list("abcde"), sep="_"))  # Cat a list-like object (same len)

# %% Pattern counting
s = pd.Series(['A', 'B', 'Aaaa', 'Bab', None])
print(s.str.count("a"))  # Case-sensitive count
print(s.str.lower().str.count("a"))  # Case-insensitive count

# %% Pattern finding
# Note: .index is similar to .find, but is not recommended
# because it will raise an error if the pattern is not found
s = pd.Series(["I love you", "You are good", "you are yourself"])
print(s.str.find("you"))  # Return index of first occurrence
print(s.str.rfind("you"))  # Find from the right
print(s.str.findall("you"))  # Return all matches (not indexes)
print(s.str.findall("you", flags=re.IGNORECASE))  # Case-insensitive
print(s.str.findall("^you", flags=re.IGNORECASE))  # Regex pattern

# %% Pattern replacement
# Note: .str.replace also accepts re.compile() and callable objects as pattern
s.str.replace("a", "XXX")  # Normal replace (case-sensitive)
s.str.replace("a", "XXX", case=False)  # Normal replace (case-insensitive)
s.str.replace("^[t|T]", "TTT", regex=True)  # With regex

# %% Pattern extraction with .str.extract()
# This method will return FIRST match only
# By default, expand=True -> return a DF
# If expand=False AND we are extracting only one group -> return a series
s = pd.Series(["a1", "b2", "c3"], dtype="string")
print(s)
print(s.str.extract(r"(?P<letter>[ab])(?P<digit>\d)"))  # Named group
print(s.str.extract(r"([ab])?(\d)"))  # Unnamed group

# %% Pattern extraction with .str.extractall()
# This method will return all matches
s = pd.Series(["a1a2", "b1", "c1"], dtype="string")
print(s)
print(s.str.extractall("(?P<letter>[a-z])(?P<digit>[0-9])"))

# %% Pattern match checking
# Note: the bellow method can take an extra argument na=True|False
# If na=False and a match is performed on NA, then a False will be returned
# instead of <NA>
s = pd.Series(["1", "2", "3a", "3b", "03c", "4dx", None], dtype="string")
print(s)
print(s.str.fullmatch(r"[0-9][a-z]"))  # Match the pattern? (most general)
print(s.str.contains(r"[0-9][a-z]"))  # Contains letters and digits?
print(s.str.startswith("3"))  # Starts with 3?
print(s.str.endswith("x"))  # Starts with x?
print(s.str.match(r"[0-9][a-z]"))  # Match a pattern at the start of s?

# %% Replication
s = pd.Series(["a", "b", "c"], dtype="string")
print(s)
print(s.str.repeat(3))

# %% Padding
s = pd.Series(["1", "2", "11", "12"], dtype="string")
print(s)
print(s.str.pad(3, "left", "?"))  # Left pad
print(s.str.pad(3, "right", "?"))  # Right pad
print(s.str.pad(3, "both", "?"))  # Both side pad

# %% Justification
s = pd.Series(["1", "2", "11", "12"], dtype="string")
print(s)
print(s.str.ljust(3, "?"))  # Left just (right fill)
print(s.str.rjust(3, "?"))  # Right just (left fill)

# %% Zero fill
s = pd.Series(["1", "2", "11", "12"], dtype="string")
print(s)
print(s.str.zfill(3))
