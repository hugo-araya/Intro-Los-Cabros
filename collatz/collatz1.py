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

def calcular(ini, fin):
    numero = 0
    mayor = 0
    nume = ini
    while nume <= fin:
        lista = collatz(nume)
        if len(lista) > mayor:
            mayor = len(lista)
            numero = nume
        nume = nume + 1
    return numero

ini = int(input("Valor Inicial: "))
fin = int(input("Valor Final: "))
numero = calcular(ini, fin)
print(numero)
