from abc import (
    ABC,
    abstractmethod
)

from book.book import Book


class Print(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class PrintConsole(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrintBook:
    @staticmethod
    def print(book: Book, print_type: str) -> None:
        if print_type == "console":
            PrintConsole().print(book)
        elif print_type == "reverse":
            PrintReverse().print(book)
        else:
            raise ValueError(f"Unknown print type: {print_type}")