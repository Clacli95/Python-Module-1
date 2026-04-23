class Automobile:
    ruote=4

    def __init__(self, modello):
        self.modello=modello


auto1=Automobile("Fiat 500")
auto2=Automobile("Volkswagen Golf") 

print(f"Auto 1: {auto1.modello}, Ruote: {auto1.ruote}")  # Auto 1: Fiat 500, Ruote: 4
print(f"Auto 2: {auto2.modello}, Ruote: {auto2.ruote}")  # Auto 2: Volkswagen Golf, Ruote: 4