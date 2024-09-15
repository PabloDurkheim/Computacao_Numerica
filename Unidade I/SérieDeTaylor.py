#Série de Taylor
import math
from numpy import log as ln

#Pontos
x0 = 0 #"Em torno do ponto..."
x = 1
h = x - x0


#escreva a função aqui no return
def funcao(x):

  return -0.1*pow(x,4) -0.15*pow(x,3) -0.5*pow(x,2) -0.25*x + 1.2

#escreva 1ª derivada aqui no return
def der1(x):

  return -0.1*4*pow(x,3) -0.15*3*pow(x,2) -0.5*2*x -0.25

#escreva 2ª derivada aqui no return
def der2(x):

  return -0.1*4*3*pow(x,2) -0.15*3*2*x -0.5*2 

#escreva 3ª derivada aqui no return
def der3(x):

  return 0

#escreva 4ª derivada aqui no return
def der4(x):

  return 0

#escreva 5ª derivada aqui no return
def der5(x):

  return 0
  
#Acrescente outros caso precise
T0 = funcao(x0)
T1 = T0 + der1(x0)*h
T2 = T1 + (der2(x0)*pow(h,2))/math.factorial(2)


#Erro relativo
Er0 = abs((funcao(x)-T0)/funcao(x))
Er1 = abs((funcao(x)-T1)/funcao(x))
Er2 = abs((funcao(x)-T2)/funcao(x))


print("Diretamente no ponto, f(",x,") = ", funcao(x),"\n")
print("Taylor de ordem 0 = ",T0)
print("Erro relativo: ", Er0,"\n")
print("Taylor de ordem 1 = ",T1)
print("Erro relativo: ", Er1,"\n")
print("Taylor de ordem 2 = ",T2)
print("Erro relativo: ", Er2,"\n")
