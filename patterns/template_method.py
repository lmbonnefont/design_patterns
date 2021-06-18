# Template method design pattern
# The goal of this design pattern is to define the behavior of a recipe (3 steps, prepare, cook, clean)
# Leaving space for the implementation of each recipe
from abc import ABC


class AbstractRecipe(ABC):
    def execute(self):
        """
        Main function in charge of executing the full recipe. Will not be changed by children classes
        """
        self.prepare()
        self.cook()
        self.clean()

    def prepare(self):
        raise NotImplementedError

    def cook(self):
        raise NotImplementedError

    def clean(self):
        raise NotImplementedError


class PouletFermier(AbstractRecipe):
    """
    Concrete class of AbstractRecipe. Will define its own prepare, cook and clean but not execute as all recipes should
    behave the same.
    """
    def prepare(self):
        print("Collecting the chicken and potatoes")
        print("Sharpening my knife")

    def cook(self):
        print("Placing the chicken in oven")

    def clean(self):
        print("I am cleaning this mess")

class RizAuLait(AbstractRecipe):
    """
    Concrete class of AbstractRecipe. But here the dev forgot to implement the cook method. An error should be raised
    because this recipe does not behave as the other!
    """

    def prepare(self):
        print("Collecting the rice and vanilla")
        print("Sharpening my knife")

    def clean(self):
        print("I am cleaning this mess")

if __name__ == '__main__':
    PouletFermier().execute()
    RizAuLait().execute()
