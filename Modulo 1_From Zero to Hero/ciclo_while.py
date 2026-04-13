while True:
    numero = int(input("Scrivi un numero ( > 0 ): "))
    if numero <= 0:
        print("Il numero deve essere positivo! Riprova.")
        continue
    print(f"Hai inserito il numero positivo: {numero}")
    if numero == 20:
        print("Hai inserito 20, il programma si ferma.")
        break
