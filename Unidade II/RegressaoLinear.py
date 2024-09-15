#Regressão Linear

import numpy as np
import math

vetor = np.array([1,2,3], dtype = float)
y = np.array([1,2.7,9.7], dtype = float)
elemento = 3
soma = 0;

for i in range(0, elemento):
	soma += pow(math.e, vetor[i])*y[i]

print(soma)
