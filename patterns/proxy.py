# Proxy design pattern
# Control to protect the access to some underlying resource without changing the interface
# There 3 types of Proxy:
# Remote: controls access to a resource outside of the application namespace
# Virtual: controls access to a resource that is expansive to create (// caching)
# Protection: controls access to a resource (access manager) -> Right to make the call
from time import sleep


class BookParser:
    def __init__(self, text: str):
        # The book parser takes very long to instanciate
        sleep(4)
        self.text = text

    def get_number_of_words(self):
        return len(self.text.split())

class BookParserProxy(BookParser):
    def __init__(self, text: str):
        self.text = text
        self.book_parser = None
        self.nb_of_page = None


    def get_number_of_words(self):
        if not self.book_parser:
            self.book_parser = BookParser(text=self.text)

        if not self.nb_of_page:
            sleep(3)
            self.nb_of_page = self.book_parser.get_number_of_words()
        return self.nb_of_page



if __name__ == '__main__':
    # In this example we switch the delay the cost of the object creation to when it is used.
    # In other word, it is cheap to create object but expansive to use it the first time, where before it was expansive to create but cheap to use it.
    # This is useful when we use objects as 'wrappers' but do not call functions of this object.
    # We can also implement caching on the object to decrease the cost of calling get_number_of_words

    text1 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair."

    a = BookParserProxy(text1)
    print("Created first proxy. No cost at creation.")

    print(f"1st time we get the number of words. We need to actually get the number of words, it's sooo long. We will store it for later use")
    print(a.get_number_of_words())

    print(f"2ond time we get the number of words. It is so much quicker because we access the cached value!")
    print(a.get_number_of_words())


