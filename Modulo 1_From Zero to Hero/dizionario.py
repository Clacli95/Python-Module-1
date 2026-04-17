studente = {"NOME" : "Luca" , "età" : 20 , "corso" : "mediazione linguistica" }
studente["matricola"]= 2939
print(studente.get("NOME"))
for k,v in studente.items():
    print(k,v)
