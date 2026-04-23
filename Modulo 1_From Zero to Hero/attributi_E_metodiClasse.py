class Studente:
    scuola="Liceo Classico"

    def __init__(self, nome):
        self.nome = nome

    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e frequento il {self.scuola}.") 

    @classmethod
    def cambia_scuola(cls, nuova_scuola):
        cls.scuola = nuova_scuola   

s1= Studente("Giulia")
s2= Studente("Marco")
s1.presentati()  # Ciao, mi chiamo Giulia e frequento il Liceo Classico.
s2.presentati()  # Ciao, mi chiamo Marco e frequento il Liceo Classico.
Studente.cambia_scuola("Liceo Scientifico")
s1.presentati()  # Ciao, mi chiamo Giulia e frequento il Liceo Scientifico.
s2.presentati()  # Ciao, mi chiamo Marco e frequento il Liceo Scientifico.
    