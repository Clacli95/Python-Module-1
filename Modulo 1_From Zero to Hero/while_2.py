somma = 0  # Variabile per la somma totale

while True:
    numero = int(input("Inserisci un numero positivo (o un numero negativo per uscire): "))
    
    if numero < 0:
        break  # Esci dal ciclo se il numero è negativo
    
    somma += numero  # Aggiungi il numero alla somma totale

print(f"La somma totale è: {somma}")


