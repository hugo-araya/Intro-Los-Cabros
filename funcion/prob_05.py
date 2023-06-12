
def suma_digitos(numero):
    suma = 0
    i = 0
    while i < len(numero):
        suma = suma + int(numero[i])
        i = i + 1
    return suma

numero = input("digite numero: ")
while (numero != '0'):
    suma = suma_digitos(numero)
    print(suma)
    numero = input("digite numero: ")


