# TYPE HINTS FOR VARIABLES
# General syntax
# var_name: expected_type = value

from typing import Optional, Union, Any

# %% Simple built-in types
x1: int = 1
x2: float = 2
x3: bool = True
x4: str = "Tue"

# %% Assignment is optional
# No value at runtime until assigned
age: int

# %% Use Optional for values that could be None
val: Optional[str]

# %% Use Union when something could be one of several types
a_list: list[Union[int, float, str]] = ["Hello", 1, 1.5]

# %% Use Any if you are not so sure about the type (it is too dynamic)
flex: Any
