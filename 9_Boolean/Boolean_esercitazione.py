età = int(input("Quanti anni hai?"))
patente = input("Hai la patente? sì/no")
ha_patente = età >= 18
print (bool(ha_patente))




ritardo = input("Sei in ritardo con la consegna del libro? (sì/no) ").lower() == "sì"


utente_premium = input("Sei un utente premium? (sì/no) ").lower() == "sì"


puo_entrare = not ritardo or utente_premium


print("Può entrare :",puo_entrare)

