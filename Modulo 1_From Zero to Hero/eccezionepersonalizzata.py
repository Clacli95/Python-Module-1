class Etanegativa(Exception):
    pass

class Studente:
    def __init__(self, età):
        if età < 0:
            raise Etanegativa("L'età non può essere negativa.")
        self.età = età

try:    studente = Studente(-5)
except Etanegativa as e:
    print(e)    


#secondo esercizio

class ProdottoEsaurito(Exception):
    pass

class Magazzino:
    def __init__(self, prodotto, quantità):
        self.prodotto = prodotto    
        self.quantità = quantità

    def rimuovi_prodotto(self, quantità):
        if self.quantità < quantità:
            raise ProdottoEsaurito("Il prodotto è esaurito.")
        self.quantità -= quantità

try:
    magazzino = Magazzino("Computer", 10)
    magazzino.rimuovi_prodotto(15)
except ProdottoEsaurito as e:
    print(e)


