def sumar(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma

def multiplicar(lista):
    multi = 1
    for numero in lista:
        multi = multi * numero
    return multi

lista = [1,2,3,4]
resultado1 = sumar(lista)
resultado2 = multiplicar(lista)
print(resultado1)
print(resultado2)
