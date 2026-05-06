class Animale:
    def __init__(self,nome):
        self.nome=nome

def verso(self):
    pass

class Cane(Animale):
    def verso(self):
        print(f"{self.nome} dice: Bau!")

class Gatto(Animale):
    def verso(self):
        print(f"{self.nome} dice: Miao!")

cane=Cane("Fido")
gatto=Gatto("Whiskers") 

cane.verso()  # Output: Fido dice: Bau!
gatto.verso()  # Output: Whiskers dice: Miao!



class Macchinetta_caffè:
    def __init__(self, marca):
          self.marca=marca
    
    def tipologia_caffè(self):
        pass    

class Espresso(Macchinetta_caffè):
    def tipologia_caffè(self):
        print(f"{self.marca} prepara un espresso.") 

class Cappuccino(Macchinetta_caffè):
    def tipologia_caffè(self):
        print(f"{self.marca} prepara un cappuccino.")

macchinetta1=Espresso("DeLonghi")
macchinetta2=Cappuccino("Nespresso")

macchinetta1.tipologia_caffè()  # Output: DeLonghi prepara un espresso.
macchinetta2.tipologia_caffè()  # Output: Nespresso prepara un
