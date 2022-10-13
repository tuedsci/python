# INHERITANCE

from typing import ClassVar


# %% All user-defined class are implicitly inherited from the object class
# The two following syntax are equivalent
class C1:
    pass


class C2(object):
    pass


# %% Example of non-trivial inheritance
class Contact:
    all_contacts: ClassVar[list["Contact"]] = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return "{}(name='{}', email='{}')" \
            .format(self.__class__.__name__, self.name, self.email)


# %% Init 2 contacts and check the class variable Contact.all_contacts
c1 = Contact("Tue", "tue@example.com")
c2 = Contact("Hoa", "hoa@example.com")
print(Contact.all_contacts)

# %% Although we can access the class variable via an instance,
# it is not recommended
print(c1.all_contacts)


# If we try to assign c1.all_contacts to something,
# we will create an instance variable
# and the class variable is still intact

# %% Create class Supplier inherited from Contact
class Supplier(Contact):
    def send(self, pkg: str) -> None:
        print(f"{self.name} is sending a {pkg}")


# Init a supplier
s = Supplier("Tue", "tue@example.com")
print(s)
s.send("TV")


# %% Create a Friend class extending Contact
# and overwrite its constructor
# We can call .super() to invoke all functionality of the super class
class Friend(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        super().__init__(name, email)
        self.phone = phone


# Adding a new friend
f = Friend("Danh", "danh@example.com", "0909123456")
print(f)
