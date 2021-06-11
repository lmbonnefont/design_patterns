# Decorator design system
from abc import ABC


class Beverage(ABC):
    def cost(self):
        raise NotImplementedError


class Coffee(Beverage):
    def cost(self):
        return 4.3


class Espresso(Beverage):
    def cost(self):
        return 3

class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

class WhippedDecorator(BeverageDecorator):
    def cost(self):
        return self.beverage.cost() + 2

class SoyDecorator(BeverageDecorator):
    def cost(self):
        return self.beverage.cost() + 1

if __name__ == '__main__':
    # This design pattern is about adding options to a base class
    # Here for instance we add options such as whipped cream to a beverage
    # Instead of creating multiple classes CoffeeWithWhipped, CoffeeWithSoy, CoffeeWithSoyAndWhipped or add booleans to specify if the beverage has or not a topping
    # We decide to encapsulate the Coffee in decorators.
    # Those decorators are agnostic of what they encapsulate, it only have to be a beverage (Component concrete (Actual beverage) or another decorator)
    # Similarly to a recursive approach, the layer will call the child layer cost function and add the cost of the topping on it
    # Problem is as it is agnostic we cannot have some stuff as "1 chocolate topping is 3 euros, the second is 2"

    print(SoyDecorator(WhippedDecorator(Coffee())).cost())
