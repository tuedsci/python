# PROPERTIES

# %% Python favors direct access to the attributes over a bunch of
# setters and getters
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


# %% Sometimes, we want to pack a logic when setting or getting some
# attribute, then we can write a setter and a getter and pack them
# into a property as in the following example
# Note: attribute with _ prefix means for internal use only
# (i.e., not part of the public interface)
class Person:
    def __init__(self, name: str | None = None) -> None:
        self._name = name

    def _set_name(self, name: str) -> None:
        print("Some logic when setting name")
        self._name = name

    def _get_name(self) -> str:
        print("Some logic when getting name")
        return self._name

    def _del_name(self) -> None:
        del self._name

    name = property(_get_name, _set_name, _del_name, "Documentation here")


# Test
p = Person()  # Init
p.name = "Tue"  # Set name
print(p.name)  # Get name


# %% We can create properties using decorators
# This is very common when we want a method to be treated as if
# it were an attribute
class Scores(list[float]):
    @property
    def average(self) -> float:
        return sum(self) / len(self)

    @property
    def min(self):
        return min(self)

    @property
    def max(self):
        return max(self)


# Test
s = Scores([1, 2, -3])
print(s)
print(f"avg={s.average!r}, min={s.min!r}, max={s.max!r}")

# %% Some guidelines
# - Use methods for actions, i.e., things that can be done to or performed on
#   the object. Methods are usually verbs
# - Use attributes/properties for state of the object, i.e., the data that
#   the object holds. Attributes are often nouns, adjectives, or prepositions
#   that describe the object
#       - Ordinary (non-property) attributes is initialized in __init__()
#       - Use properties for exceptional cases where there's a need for
#         some logic when perform getting and setting the attribute such as
#         authentication, data validation.
#       - We can use properties for lazy attributes
