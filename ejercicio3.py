'''Construir una función que reciba como
parámetro un vector de 10 posiciones
enteras y retorne la posición del mayor
número primo almacenado en el vector'''



def vector():
    Arreglo = [[1, 5, 8, 3, 4, 9, 8, 3, 4, 7, 9]]

    for i in range(0, 11):
        div = 0
        for j in range(0, 11):
            if Arreglo % j == 0:
                div = div + 1

        if div == 2:
            menor = mayor = Arreglo[0]
            for k in range(1, Arreglo):
                if Arreglo > mayor:
                    mayor = Arreglo
            if Arreglo < menor:
                menor = Arreglo

        print(f"El primo mayor es ", mayor)


    return Arreglo


