# TYPE HINTS FOR CLASSES

from typing import ClassVar


# %% Declare instance variable
class Word:
    max_len: int
    chars: list[str]


# %% Declare type of attr in __init__
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


p = Point(3, 5)
print(p.x, p.y)


# %% User-defined classes are valid for annotation
# First, we creat a BankAccount class
# We do not need annotation for self because it can be inferred
# from the annotations of params
class BankAccount:
    def __init__(self, holder: str, balance: float = 0) -> None:
        self.holder = holder
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        self.balance -= amount


# Now we can use BankAccount in annotation
def transfer(src: BankAccount, dst: BankAccount, amount: float) -> None:
    src.withdraw(amount)
    dst.deposit(amount)


# Now we test
a = BankAccount("A", 100)
b = BankAccount("B", 50)
transfer(a, b, 30)
print(a.balance, b.balance)


# %% Annotate class variable explicitly with ClassVar
class Contacts:
    all_contacts: ClassVar = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)


a = Contacts("Tue", "tue@example.com")
print(a.all_contacts, a.name, a.email)
