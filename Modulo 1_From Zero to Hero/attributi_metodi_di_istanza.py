class Studente :
    def __init__(self, nome, età):
        self.nome=nome
        self.età=età  
    
    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.età} anni.")

s1 = Studente("Alice", 20)
s2 = Studente("Bob", 22)    

s1.presentati()  # Ciao, mi chiamo Alice e ho 20 anni.
s2.presentati()  # Ciao, mi chiamo Bob e ho 22 anni.

s1.corso="Informatica"  # Aggiunta dinamica di un nuovo attributo all'istanza s1
print(f"Ciao, mi chiamo Alice e ho 20 anni e Studio {s1.corso}")  # Informatica