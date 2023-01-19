class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс-конструктор бумажная книга, потомок класса Book"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.set_pages(pages)

    def set_pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError("Check pages type")
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Класс-конструктор аудио-книги, потомок класса Book"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.set_duration(duration)

    def set_duration(self, duration):
        if not isinstance(duration, float):
            raise TypeError("Check duration type")
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

if __name__ == "__main__":
    audio1 = AudioBook('My audio book','Ivan Ivanov',60.0)
    paper1 = PaperBook('My paper book','Petr Petrov', 1000)