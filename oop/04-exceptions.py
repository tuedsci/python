# EXCEPTIONS
# TODO: further topics
#   - Write user-defined exception classes

# %% An exception in Python is an object instantiated from some exception
# classes, which inherited from the BaseException class
# Examples
# - SyntaxError
# - NameError
# - ZeroDivisionError
# - IndexError
# - KeyError
# - TypeError
# - AttributeError
print(issubclass(Exception, BaseException))  # True
print(issubclass(SyntaxError, Exception))  # True
print(issubclass(SyntaxError, ValueError))  # False


# %% Create EvenOnly class extending from list, which overrides .append()
# method with exception handling
class EvenOnly(list[int]):
    def append(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Can only append an integer")

        if value % 2 != 0:
            raise ValueError("Can only append even integer")

        super().append(value)


# e_list = EvenOnly()
# e_list.append(5) -> will raise a ValueError
# e_list.append(1.4) -> will raise a TypeError
# To be complete, we also need to overwrite other methods like
# .insert(), .extend(), ...


# %% Handle an exception with try except
def div(a: float, b: float) -> float:
    try:
        return a / b
    except Exception as e:
        print(f"Hey! Watch out for {e!r}")


div(5, 0)  # ZeroDivisionError


# %% Deal with multiple exceptions
# - except: we can use it multiple times (like elif) to catch an exception
# - else: we use it at most once to do something if there is no exception
# - finally: we use it at most once as a clean-up code (it always runs
#   regardless if we encounter an exception or not). It is good for tasks
#   such as closing an open DB/file connection
#   One note about finally that it is post-return
def div_2(a: float, b: float) -> float:
    try:
        r = a / b
    except TypeError:
        print("You must provide two numeric arguments")
    except ZeroDivisionError:
        print("b must be different from 0")
    else:
        return r
    finally:
        print("This is a clean-up code that always runs")
        print("For example: 'I am closing the file connection'")

# div_2("a", 2)  # TypeError
# div_2(1, 0)  # ZeroDivisionError
# div_2(1, 2)  # OK

# %% Note on philosophy
# EAFP: Easier to Ask for Forgiveness than Permission
#   meaning execute the code and deal with whatever goes wrong
# LBYL: Look Before You Leap
#   meaning think carefully about what could go wrong
# Python programmers often adopt the EAFP approach
