# ABSTRACT BASE CLASSES
from abc import ABCMeta, abstractmethod


# %% Extend from ABC
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def eat(self, food: str) -> None: pass

    @property
    @abstractmethod
    def can_walk(self) -> bool: pass


class Cat(Animal):
    def eat(self, food: str) -> None:
        pass

    @property
    def can_walk(self) -> bool:
        return True
