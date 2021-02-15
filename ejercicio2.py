'''Leer dos matrices 5x5 entera y determinar
si el promedio de los mayores elementos
que pertenecen a la serie de Fibonacci de
cada fila de una matriz es igual al
promedio de los mayores elementos que
pertenecen a la serie de Fibonacci de
cada fila de la otra matriz.'''

import numpy as np

a=0
b=1
c=int
d=int
nf=0
promedio1=bool
promedio1=False
promedio2=False

matriz1=[[]]
matriz2=[[]]

nf=int(input("Ingrese la cantidad de elementos para la serie fibonacci"))
for i in range(0,5):
      for j in range(0,5):
          for k in range(0,nf):
              c=a+b
              a=b
              b=c
              d=c

print(matriz1[c[d]])

promedio1=True

a = 0
b = 1
c = int
d = int
nf = 0
promedio1 = bool
promedio1 = False
promedio2 = False

matriz1 = [[]]
matriz2 = [[]]

nf = int(input("Ingrese la cantidad de elementos para la serie fibonacci"))
for i in range(0, 5):
    for j in range(0, 5):
        for k in range(0, nf):
            c = a + b
            a = b
            b = c
            d = c

print(matriz2[c[d]])

promedio2 = True



if promedio1 == promedio2:
    print(f"Son iguales")

else:
    print(f"No son iguales")
