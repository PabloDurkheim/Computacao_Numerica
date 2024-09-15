#Integração - regra 3/8
import math
from numpy import log as ln
import numpy as np

#defina os limites e o nº de subintervalos
a = 0
b = 1.2
n = 6
h = (b-a)/n

#nao mexer
x = np.linspace(a, b, n+1)
y = []

#defina a função da integral
def funcao(x):
	return ( pow(math.e, x)*math.cos(x) )

#fórmula: I = (h/2)*(y0 + 2y1+2y2...+y6)

print("INTEGRAL - REGRA DE SIMPSON 3/8", "\n")

#calcula o y - não mexer
for i in range (0, n+1):
	x[i] = round(x[i],3)
	y.append( round( funcao(x[i]),3 ) )

#mostra na tela - não mexer
for i in range (0, n+1):
	print("x",i,"=",x[i]," | y",i,"=",y[i])

#calcula a integral
soma = 0
cont = 0
for i in range(0, n+1):
	if(i == 0 or i == n):
		soma += y[i]
	else:
		if(cont <= 2):
			soma += 3*y[i]
			cont = cont + 1
		else:
			soma += 2*y[i]
			cont = 0

I = round( 3*(h/8)*soma, 3 )

print()
print("I =",I)
