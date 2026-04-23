class Persona:
    def __init__(self, nome):
        self.__nome = nome  # attributo privato con __

    def get_nome(self):  # metodo dedicato per leggere il nome
        return self.__nome

    def presentati(self):
        return f"Ciao, sono {self.__nome}!"


class Studente(Persona):
    def __init__(self, nome, corso):
        super().__init__(nome)
        self.corso = corso

    def presentati(self):  # override del metodo della classe padre
        return f"Ciao, sono {self.get_nome()} e frequento il corso di {self.corso}!"


# Test
s = Studente("Mario", "Informatica")
print(s.presentati())       # Ciao, sono Mario e frequento il corso di Informatica!
print(s.get_nome())         # Mario
