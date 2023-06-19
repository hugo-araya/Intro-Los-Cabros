def es_par(numero):
    if numero%2 == 0:
        return True
    else:
        return False
    
def collatz(numero):
    lista = [numero]
    while numero != 1:
        if es_par(numero):
            numero = numero // 2
        else:
            numero = numero*3 + 1
        lista.append(numero)
    return lista

numero = int(input("Numero: "))
lista = collatz(numero)
print(lista)
print('Cantidad de elementos: ',len(lista))
