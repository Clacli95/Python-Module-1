#cercare

import numpy as np
a = np.array([1, 2, 3, 4, 5,6,7,8,3,9,7,8,3])
idx= np.where(a == 3)
print(idx)

#filtrare
a = np.array([1, 2, 3, 4, 5,6,7,8,3,9,7,8,3])
filtro = a > 5
print(a[filtro])

#ordinare
a = np.array([1, 2, 3, 4, 5,6,7,8,3,9,7,8,3])
a_ordinato = np.sort(a)
print(a_ordinato)