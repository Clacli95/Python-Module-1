import numpy as np

a = np.array([[1, 2], [3, 4]])
vec_zero = np.zeros(5, dtype=int)
vec_ones = np.ones(5, dtype=int)

print("Il mio array a \n", a)
print("dimensione", a.shape)
print(a.flatten())
print("Il mio vettore di zeri \n", vec_zero)
print("Il mio vettore di uno \n", vec_ones)
print("Il mio vettore pieno di 3 \n", 3* vec_ones)

range_vec = np.arange(2, 10, 3)    # start=2, stop=9
print("Il mio vettore con arange \n", range_vec)
lin_vec = np.linspace(0, 1, 6)
print("Il mio vettore con linspace \n", lin_vec)

a_cla = 100000* np.random.rand(200)
print("Il mio array con numeri casuali \n", a_cla)

a_cla_casa= np.array(["casa", "tavolino", "clipper", "libro", "sedia", "divano"])
# a_cla_casa = a_cla_casa.reshape(2, 3)
# print("Il mio oggetto preferito è:", a_cla_casa[-1])
print("A casa c'è il", a_cla_casa[1:4:2])
print(a_cla_casa.base)