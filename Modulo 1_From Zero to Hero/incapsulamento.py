class ContoBancario:
    def __init__(self, saldo):
        self.__saldo = saldo

    def deposito(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo} effettuato. Saldo attuale: {self.__saldo}")
        else:
            print("Importo di deposito non valido.")

    def prelievo(self, importo):
        if 0 < importo <= self.__saldo:
            self.__saldo -= importo
            print(f"Prelievo di {importo} effettuato. Saldo attuale: {self.__saldo}")
        else:
            print("Importo di prelievo non valido o saldo insufficiente.")

    def get_saldo(self):
        return self.__saldo
    
   
conto=ContoBancario(1000)  # Creazione di un conto con saldo iniziale di 1000
conto.deposito(500)  # Deposito di 500 effettuato. Saldo attuale: 1500
conto.prelievo(200)  # Prelievo di 200 effettuato. Saldo attuale: 1300
print(f"Saldo finale: {conto.get_saldo()}")  # Saldo finale: 1300