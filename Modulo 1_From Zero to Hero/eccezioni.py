# Divisione per zero
class Divisione:
    def __init__(self, a, b):
        self.a = a
        self.b = b  

    def dividi(self):
        if self.b == 0:
            raise ValueError("Il denominatore non può essere zero.")
        return self.a / self.b

# Creiamo un oggetto Divisione e proviamo a dividere
try:
    divisione = Divisione(10, 0)
    risultato = divisione.dividi()
    print("Risultato della divisione:", risultato)
except ValueError as e:
    print(e)

# Persona che invecchia
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def invecchia(self, anni):
        if anni < 0:
            raise ValueError("Gli anni devono essere un numero positivo.")
        self.eta += anni

# Creiamo un oggetto Persona e invecchiamolo
persona = Persona("Mario", 30)
try:
    persona.invecchia(5)
    print(f"{persona.nome} ha ora {persona.eta} anni.")
except ValueError as e:
    print(e)

# Prelevare da un conto bancario
class ContoBancario:
    def __init__(self, saldo):
        self.saldo = saldo

    def preleva(self, importo):
        if importo > self.saldo:
            raise ValueError("Fondi insufficienti.")
        self.saldo -= importo

# Creiamo un oggetto ContoBancario e proviamo a prelevare
conto = ContoBancario(100)
try:
    conto.preleva(60)
    print("Saldo residuo:", conto.saldo)
except ValueError as e:
    print(e)