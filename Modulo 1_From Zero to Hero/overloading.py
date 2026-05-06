import math

class Frazione:
    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore
        self.simplify()

    def simplify(self):
        gcd = math.gcd(self.numeratore, self.denominatore)
        self.numeratore //= gcd
        self.denominatore //= gcd

    def __add__(self, other):
        nuovo_num = self.numeratore * other.denominatore + other.numeratore * self.denominatore
        nuovo_den = self.denominatore * other.denominatore
        result = Frazione(nuovo_num, nuovo_den)
        return result

    def __str__(self):  
        return f"{self.numeratore}/{self.denominatore}"

# Esempio d'uso:
f1 = Frazione(1, 2)
f2 = Frazione(1, 4)  # Modificato il denominatore
somma = f1 + f2
print(somma)  # Dovrebbe stampare 3/4
