class Studente:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    @classmethod
    def da_stringa(cls, stringa):
        nome, eta = stringa.split("-")
        return cls(nome, int(eta))

    @property
    def anno_eta(self):
        return 2026 - self.eta

    @anno_eta.setter
    def anno_eta(self, value):
        if value < 2026:
            self.eta = 2026 - value
        else:
            print("L'anno di nascita non può essere nel futuro.")

S= Studente.da_stringa("Luca-20")
print("Anno di nascita iniziale: ", S.anno_eta)  # Output: Luca
S.anno_eta = 2000
print("Anno di nascita aggiornato: ", S.anno_eta)  # Output: 2000   