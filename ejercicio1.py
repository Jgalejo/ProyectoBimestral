'''
Leer n números enteros,
almacenarlos en un vector y
determinar en qué posición está el
menor número primo.
'''

n=int(input("Ingrese el tamaño del arreglo"))
Arreglo=[]

for i in range(0,n):
    a = int(input("Ingrese los elementos"))
    Arreglo.append(a)
    div=0
    for j in range(1,Arreglo):
        if Arreglo%j==0:
            div=div+1
if div==2:
    menor=mayor=Arreglo
    for k in range(1,n):
        if Arreglo>mayor:
            mayor=Arreglo
        if Arreglo<menor:
            menor=Arreglo

        print(f"El primo menor es: ",menor)

print(Arreglo)


