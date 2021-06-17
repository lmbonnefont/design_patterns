#Chain of command pattern
from abc import ABC
from typing import Optional


class Handler(ABC):
    def __init__(self, next_handler: Optional["Handler"] = None):
        self.next_handler = next_handler

    def handle(self, amount: int):
        raise NotImplementedError

class HandlerFifty(Handler):
    def handle(self, amount: int):
        nb_of_notes = amount // 50
        residual = amount % 50
        print(f"{nb_of_notes} notes of 50")
        if residual:
            self.next_handler.handle(amount=residual)


class HandlerTwenty(Handler):
    def handle(self, amount: int):
        nb_of_notes = amount // 20
        residual = amount % 20
        print(f"{nb_of_notes} notes of 20")
        if residual:
            self.next_handler.handle(amount=residual)


class HandlerTen(Handler):
    def handle(self, amount: int):
        nb_of_notes = amount // 10
        print(f"{nb_of_notes} notes of 10")


class ATMMachine:
    def __init__(self):
        self.handler_ten = HandlerTen()
        self.handler_twenty = HandlerTwenty(next_handler=self.handler_ten)
        self.handler_fifty = HandlerFifty(next_handler=self.handler_twenty)

    def withdraw(self, amount: int):
        self.handler_fifty.handle(amount)

if __name__ == '__main__':
    """
    The chain of command pattern splits a task (here determine how an amount should be splitted in notes),
    into different steps that process something (here each step is responsible to determine how many note of 50, 20, 10
    Should be distributed and then calls the next handler if needed.
    Note about it: it's a shame that a lot of code is duplicated between handler in this example :/ 
    """
    amount = None
    atm = ATMMachine()
    while not amount:
        response = input("Enter an amount you wish to withdraw: ")
        try:
            amount = int(response)
        except ValueError:
            print("Enter a valid amount to withdraw")

        if amount < 10 or amount % 10 != 0:
            print("The amount must be greater than 10 and a multiplier of 10")

    atm.withdraw(amount)
    print("Here are your notes")
