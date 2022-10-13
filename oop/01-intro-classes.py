# INTRODUCTION TO CLASSES

# %% Define the first simple class
class FirstClass:
    pass


# Instantiate objects
a = FirstClass()
b = FirstClass()

# Verify a and b are 2 different objects
print(a)
print(b)
print(a is b)

# We can add attributes to the object by direct assignments
# Although it is not recommended
a.x = "A"
b.y = "B"
print(a.x, b.y)


# %% A better approach is to explicitly define all attributes
class Point:
    """
    Represents a point in 2D space
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Init the position of a new point
        :param x: x-coord
        :param y: y-coord
        """
        self.x = x
        self.y = y

    def move(self, dx: float, dy: float) -> None:
        """
        Moves a point
        :param dx: change in x-coord
        :param dy: change in y-coord
        :return:
        """
        self.x += dx
        self.y += dy


# %% Init 2 objects
p1 = Point()
p2 = Point(1, 2)
print(p1.x, p1.y)
print(p2.x, p2.y)

# %% When calling an instance method, imagine the object itself is an
# implicit argument passed to the method (the self param)
p1.move(1, 1)
p2.move(1, 1)
print(p1.x, p1.y)
print(p2.x, p2.y)
