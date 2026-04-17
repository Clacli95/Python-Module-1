corso_A = {"Claudia","Luca","Gianni","Gianmarco"}
print("Corso A:", corso_A)
corso_B = {"Laura", "Gianpiero", "Pasquale", "Denise"}
print("Corso B:", corso_B)

almeno_un_corso = corso_A | corso_B
print("Frequentano almeno un corso:", almeno_un_corso)
print("Frequentano solo corso_A:" , corso_A - corso_B)
print("Frequentano solo corso_B:" , corso_B - corso_A)

studenti_unici = len(almeno_un_corso)
print("Numero di studenti unici:", studenti_unici)