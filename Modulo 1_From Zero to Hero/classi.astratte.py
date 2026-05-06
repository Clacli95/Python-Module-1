from abc import ABC, abstractmethod

class Veicolo(ABC):
    @abstractmethod
    def muovi(self):
        pass

class Auto(Veicolo):
    def muovi(self):
        print("L'auto si muove su strada .")
    
class Aereo(Veicolo):
    def muovi(self):
        print("L'aereo vola nel cielo.")

auto = Auto()
aereo = Aereo() 
auto.muovi()  # Output: L'auto si muove su strada.
aereo.muovi()  # Output: L'aereo vola nel cielo.    

