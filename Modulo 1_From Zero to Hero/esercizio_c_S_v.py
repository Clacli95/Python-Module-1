import csv

class GestoreLibriCSV:
    def __init__(self, nome_file):
        self.nome_file = nome_file

    def leggi(self):
        with open(self.nome_file, 'r') as file:
            return list(csv.DictReader(file))
        
    
# Esempio di utilizzo
gestore = GestoreLibriCSV("prova.csv")
libri = gestore.leggi()
print(libri)
