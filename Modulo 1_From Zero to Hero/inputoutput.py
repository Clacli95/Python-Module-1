class Studente:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.età} anni.") 

#secondo esercizio

    def __str__(self):
        return f"Studente: {self.nome}, Età: {self.età}"

# Creiamo un oggetto Studente e chiamiamo il metodo presentati
studente = Studente("Alice", 20)            
studente.presentati()
print(studente)

#terzo esercizio

class Diario:
    def __init__(self, file_name):
        self.file_name = file_name
       

    def scrivi_diario(self, messaggio):
        with open(self.file_name, 'a') as file:
            file.write(messaggio + '\n')

diario = Diario("diario.txt")
diario.scrivi_diario("Oggi è stata una giornata fantastica!")   

print("Il messaggio è stato scritto nel diario.")   