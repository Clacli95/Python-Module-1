class Studente:
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso

    def presentati(self):
        # Metodo interno alla classe con self
        print(f"Ciao, mi chiamo {self.nome} e studio {self.corso}.")

# Creare istanze fuori dalla classe
studente1 = Studente("Claudia", "Informatica")
studente2 = Studente("Luca", "Matematica")

# Chiamare il metodo su ciascuna istanza
studente1.presentati()  # Output: Ciao, mi chiamo Claudia e studio Informatica.
studente2.presentati()  # Output: Ciao, 