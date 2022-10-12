# TYPE HINTS FOR FUNCTIONS
# General syntax
# def func_name(param: param_type) -> out_type

from typing import Iterator, Union


# %% One param
def int_to_str(n: int) -> str:
    return str(n)


int_to_str(10)


# %% Multi param
def add(a: float, b: float) -> float:
    return a + b


add(10, 7)


# %% Default arg
def say_hi(name: str = "user") -> None:
    print(f"Hello {name}")


say_hi()
say_hi("Tue")


# %% A generator function that yields int elements
def gen(n: int) -> Iterator[int]:
    for i in range(n):
        yield i


print(gen(5))
print(list(gen(5)))


# %% Multi line annotation
def crawl_page(
        url: Union[str, list[str]],
        parse: bool,
        wait: int
) -> bool:
    pass


# %% For a generator, we should use Iterator as return type (not Iterable)
# Rule of thumb: annotate functions with most specific return type possible
def n_squares(n: int) -> Iterator[int]:
    for i in range(n):
        yield i ** 2


print(n_squares(5))
print(list(n_squares(5)))
