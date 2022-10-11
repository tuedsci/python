# TYPE HINTS FOR BUILT-IN TYPES
# General syntax
# var_name: collection_type[element_type] = value

from typing import List, Set, Iterable

# %% Python 3.9+
# The built-in type can be used directly
list_of_ints: list[int] = [1, 7, 3, 9]
set_of_strs: set[str] = {"Tue", "Hoa", "Timon"}

# %% Python <= 3.8
# The collection types must be imported from typing module
# and the type names are capitalized
list_of_bools: List[bool] = [True, True, False]
set_of_floats: Set[float] = {1.5, 2.7, 3.8}

# %% For mapping, we need types for both keys and values
d: dict[str, int] = {"US": 1, "CA": 2}

# %% For tuples of fixed size, we specify types of all elements
t: tuple[str, int, float] = ("Tue", 20, 1.85)


# %% Accept an iterables arguments
def ints_to_strs(ints: Iterable[int]) -> list[str]:
    return [str(x) for x in ints]


print(ints_to_strs([1, 2, 3]))
print(ints_to_strs((1, 2, 3)))
print(ints_to_strs({1, 2, 3}))
