class Forma:
    def __init__(self, nome):
        self.nome = nome

    def area(self):
        pass    

class Rettangolo (Forma):
       def area(self, base, altezza):
            return base * altezza
        
class Cerchio (Forma):
        def area(self, raggio):
            import math
            return math.pi * raggio ** 2
        
rettangolo = Rettangolo("Rettangolo")
cerchio = Cerchio("Cerchio") 

print(f"L'area del {rettangolo.nome} è: {rettangolo.area(5, 3)}")  # Output: L'area del Rettangolo è: 15
print(f"L'area del {cerchio.nome} è: {cerchio.area(4    )}")  # Output: L'area del Cerchio è: 50.26548245743669
