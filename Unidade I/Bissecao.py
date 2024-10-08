#Método da Bissecção (sempre converge)
import math
from numpy import log as ln

#Intervalo
a = 2
b = 3

#Iteraçoes (não mexer)
iteracoes = 1
continuar = 1

#escreva a função aqui no return
def funcao(x):

  return pow(x,3)-10

#Bolzano
def bolzano(x1, x2):

  return funcao(x1)*funcao(x2)

  
#Não mexer
while(continuar == 1):

  print("Iteração ",iteracoes, "\n")
  
  #precisa torar no meio
  x = (a+b)/2

  print("x = ",x, "\n")
  
  if(bolzano(a, x) < 0):

    b = x
    print("A raiz está entre ",a, " e ",x,"\n")
    print("f(",a,") = ", funcao(a),"\n")
    print("f(",x,") = ", funcao(x),"\n")

  elif(bolzano(x, b)<0):

    a = x
    print("A raiz está entre ",x, " e ",b,"\n")
    print("f(",x,") = ", funcao(x),"\n")
    print("f(",b,") = ", funcao(b),"\n")
    
  if(x!= a):

    #erro relativo (não mexer)
    Er = abs((x-a)/x)

    #erro absoluto
    Ea = abs(x-a)

  if(x!=b):

    #erro relativo (não mexer)
    Er = abs((x-b)/x)

    #erro absoluto
    Ea = abs(x-b)
    
  print("Erro relativo: ", Er,"\n")
  print("Erro absoluto: ", Ea,"\n")
  print("Continuar? não(0) sim(1)")

  iteracoes = iteracoes+1
  continuar = int(input())
