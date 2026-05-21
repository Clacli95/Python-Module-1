class Appunti:
    def __init__(self, file_txt):
        self.file_txt = file_txt

    def scrivi(self, testo):
        with open(self.file_txt, 'a') as file:
            file.write(testo + '\n')

    def mostra(self):
        with open(self.file_txt, 'r') as file:
            contenuto = file.read()
        print(contenuto)

    def cancella(self):
        open(self.file_txt, 'w').close()

# Esempio di utilizzo
appunti = Appunti("note.txt")
appunti.scrivi("Prima riga di appunti.")
appunti.scrivi("Seconda riga di appunti.")
appunti.mostra()
appunti.cancella()