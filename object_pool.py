# Object pool design system
from exceptions import TooManyCatsAskedException, NoMoreCatException


class CatPoolMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CatPool(metaclass=CatPoolMeta):
    def __init__(self, size: int):
        names = ["Ricou", "Pilou", "Croqmou", "Voyou", "Picsou"]
        if size > 5:
            print("Cannot create more than 5 cats sorry")
            raise TooManyCatsAskedException("You asked too many cats, the maximum is 5")
        self.cats = [Cat(names[i]) for i in range(size)]

    def get_cat(self):
        if self.cats:
            print(f"Here is your cat, his name is {self.cats[0].name}. Treat him nicely.")
            return self.cats.pop(0)
        else:
            raise NoMoreCatException("No more cat available")

    def release_cat(self, cat):
        if isinstance(cat, Cat):
            self.cats.append(cat)
            print("Thank you, your cat has been reintegrated to the pool")
        else:
            raise ValueError("Cannot add anything else but cat")




class Cat:
    def __init__(self, name: str):
        self.name = name


if __name__ == '__main__':
    # The client code.
    cp1 = CatPool(size=2)
    cp2 = CatPool(size=1)

    if id(cp1) == id(cp2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    first_cat = cp1.get_cat()
    second_cat = cp1.get_cat()
    cp1.release_cat(first_cat)
    third_cat = cp1.get_cat()
