class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}."

libro=Libro("1984", "George Orwell")
print(libro)