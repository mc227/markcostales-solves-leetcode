class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        return f"Book: {self.title}, {self.author}"



if __name__ == "__main__":
    print(Book("Goosebumps","author").display())
