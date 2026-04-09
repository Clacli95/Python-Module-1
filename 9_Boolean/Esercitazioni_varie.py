Nome = "Claudia"
Età = int(30)
Città = "Napoli"

ha_patente = Età > 18
print ("Claudia ha la patente?", bool(ha_patente))

sa_guidare = Città and Età

print ("Claudia sa guidare perchè vive a Napoli e ha 30 anni?", bool(sa_guidare))

patente_data = 2013
patente_rinnovo = 2023

rinnovo = "Quante volte ha rinnovato la patente fino ad ora?"


import math 
print(rinnovo, math.floor(patente_rinnovo/patente_data))

