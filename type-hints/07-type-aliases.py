# TYPE ALIASES
# In some cases, type hints can be long and hard to read
# You can use type aliases to avoid this

# %% Make an alias for a long annotation
Number = bool | int | float


def mult(a: Number, b: Number) -> Number:
    return a * b


print(mult(5, 7))
print(mult(True, 2.5))
