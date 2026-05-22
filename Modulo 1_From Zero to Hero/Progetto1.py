#In una biblioteca digitale si vuole realizzare un piccolo sistema software per gestire libri, utenti e prestiti.Il programma deve sfruttare variabili, tipi di dati, strutture di controllo e soprattutto la programmazione orientata agli oggetti (OOP).

class Libro_base:
    def __init__(self, titolo):
        self.titolo = titolo

    def __str__(self):
        return f"In questa biblioteca è presente il libro: {self.titolo}"
    
libro1 = Libro_base("Il nome della rosa")
print(libro1)

n_intero = 5
print ("Sono disponibili "+ str(n_intero) + " copie del libro " + libro1.titolo)

n_float = 17.5
print ("Il prezzo a libro, in caso lo si volesse acquisire, è di " + str(n_float) + " euro")

libro_disponibile = True
if libro_disponibile:   
    print("Il libro è disponibile per il prestito.")
else:    print("Il libro non è disponibile per il prestito.")

print()

#Parte 2    

lista_libri = ["Il nome della rosa", "Il pendolo di Foucault", "Baudolino", "Il cimitero di Praga", "Il libro del cielo e dell'inferno"]    
print("I libri disponibili in biblioteca sono:")    
for libro in lista_libri:
    print(libro)    

copie_libri = {
    "Il nome della rosa": 5,
    "Il pendolo di Foucault": 3,
    "Baudolino": 4,
    "Il cimitero di Praga": 2,
    "Il libro del cielo e dell'inferno": 1
}

print("Il numero di copie disponibili per ogni libro è:")
for libro, copie in copie_libri.items():
    print(f"{libro}: {copie} copie")    

print()

#Parte 3

print ("Ecco a te tutti i dettagli dei libri disponibili in biblioteca:")
class Libro(Libro_base):
    def __init__(self, titolo, autore, anno, copie_disponibili):
        super().__init__(titolo)
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def __info__(self):
        return f"Libro: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Copie disponibili: {self.copie_disponibili}"       
    
libro1 = Libro("Il nome della rosa", "Umberto Eco", 1980, 5)
print(libro1.__info__())            
libro2 = Libro("Il pendolo di Foucault", "Umberto Eco", 1988, 3)
print(libro2.__info__())
libro3 = Libro("Baudolino", "Umberto Eco", 2000, 4)
print(libro3.__info__())
libro4 = Libro("Il cimitero di Praga", "Umberto Eco", 2010, 2)
print(libro4.__info__())
libro5 = Libro("Il libro del cielo e dell'inferno", "Umberto Eco", 2015, 1)
print(libro5.__info__())

print()

class Utente:
    def __init__(self, nome,eta,id_utente):
        self.nome = nome
        self.eta = eta  
        self.id_utente = id_utente

    def scheda_utente(self):
        return f"Utente: {self.nome}, Età: {self.eta}, ID: {self.id_utente}"
    
utente1 = Utente("Claudia", 25, "U001")
print(utente1.scheda_utente())
utente2 = Utente("Luca", 30, "U002")
print(utente2.scheda_utente())  
utente3 = Utente("Giulia", 22, "U003")
print(utente3.scheda_utente())
utente4 = Utente("Marco", 28, "U004")
print(utente4.scheda_utente())
utente5 = Utente("Sara", 26, "U005")
print(utente5.scheda_utente())

print()

class Prestito: 
    def __init__(self, libro, utente, giorni_prestito):
        self.libro = libro
        self.utente = utente
        self.giorni_prestito = giorni_prestito

    def dettagli_prestito(self):
        return f"Prestito: {self.libro.titolo} a {self.utente.nome} per {self.giorni_prestito} giorni"

prestito1 = Prestito(libro1, utente1, 14)
print(prestito1.dettagli_prestito())
prestito2 = Prestito(libro2, utente2, 7)
print(prestito2.dettagli_prestito())
prestito3 = Prestito(libro3, utente3, 21)
print(prestito3.dettagli_prestito())
prestito4 = Prestito(libro4, utente4, 10)
print(prestito4.dettagli_prestito())
prestito5 = Prestito(libro5, utente5, 30)
print(prestito5.dettagli_prestito())

print ()

#parte 4

def prestito_libro(libro, utente, giorni_prestito):
    if libro.copie_disponibili > 0:
        libro.copie_disponibili -= 1
        prestito = Prestito(libro, utente, giorni_prestito)
        print(f"Prestito effettuato: {prestito.dettagli_prestito()}")
    else:
        print(f"Mi spiace, il libro '{libro.titolo}' non è disponibile per il prestito.")



prestito_libro(libro1, utente1, 14)
prestito_libro(libro1, utente2, 7)
prestito_libro(libro1, utente3, 21) 

print ()

print ("Ecco a te i dettagli dei prestiti effettuati:")

print(f"Dopo i prestiti, il numero di copie disponibili per '{libro1.titolo}' è: {libro1.copie_disponibili}")
print(f"Dopo i prestiti, il numero di copie disponibili per '{libro2.titolo}' è: {libro2.copie_disponibili}")   
print(f"Dopo i prestiti, il numero di copie disponibili per '{libro3.titolo}' è: {libro3.copie_disponibili}")
print(f"Dopo i prestiti, il numero di copie disponibili per '{libro4.titolo}' è: {libro4.copie_disponibili}")
print(f"Dopo i prestiti, il numero di copie disponibili per '{libro5.titolo}' è: {libro5.copie_disponibili}") 
