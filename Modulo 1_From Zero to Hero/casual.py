import numpy as np
a = np.random.rand(5)
print("Il mio array a \n", a)


casa_clacli = np.random.randint(1, 100, size=(3, 3))
print("Il mio array casa_clacli \n", casa_clacli)   

c = np.array([1, 2, 3, 4, 5])
b = np.random.choice(c, size=3)
print("Il mio array b \n", b)

c = np.array([1, 2, 3, 4, 5])
np.random.shuffle(c)
print("Il mio array c \n", c)