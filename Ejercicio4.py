''' Elabore un algoritmo que reciba como datos de entrada un n´umero entero
positivo n y los n elementos de un vector de tama˜no n, y que regrese como
dato de salida cu´antas veces se repite el ´ultimo elemento del vector.'''


c = 0;
i = 0;
repetido = 0;
n=int(input("Ingre la cantidad de elementos del vector"))
Vector=[]
for i in range (0,n):
    a=int(input("Ingrese los elementos"))
for n in range(n,0):
    repetido=n

    if repetido==Vector:
         c=c+1

if c > 0:
    print(f"El numero {Vector} se repite {c} veces ")
