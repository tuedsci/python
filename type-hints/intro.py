# INTRODUCTION TO TYPE HINTS
from typing import Iterable, Union, Optional


# %% By default, anything in Python is dynamically typed
def greet(name):
    return f"Hello {name}"


# %% We can add type annotations (or type hints) to help an IDE such as
# Pycharm to detect potential inconsistencies related to types in your code
def say_hi(name: str) -> str:
    return f"Hi {name}"


# %% If a function does not explicitly return a value
# then set its return type of None
def print_hello(name: str) -> None:
    print(f"Hello {name}")


# %% Functions with default args
def print_hi(name: str, excited: bool = False) -> None:
    text = f"Hi {name}"
    if excited:
        text += "!!!"
    print(text)


print_hi("Tue")
print_hi("Tue", True)


# %% Annotate collections
def greet_all(names: list[str]) -> None:
    for name in names:
        print(f"Hello {name}")


greet_all(["Tue", "Hoa", "Timon"])


# %% Additional types can be imported from typing module
# for example, we want to greet all from an Iterable
def greet_all_2(names: Iterable) -> None:
    for name in names:
        print(f"Hello {name}")


greet_all_2(("A", "B", "C"))
greet_all_2({"AA", "BB", "CC"})


# %% Use Union to specify the set of expected types
def std_user_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return f"user-{user_id}"
    else:
        return user_id


print(std_user_id(5))
print(std_user_id("user-7"))


# %% Use Optional[str] to indicate that we accept only str or None
# It is similar to Union[str, None]
def make_person(name: str, place: Optional[str] = None) -> dict:
    return {"name": name, "place": place}


print(make_person("Tue", "VN"))
print(make_person("Timon"))
