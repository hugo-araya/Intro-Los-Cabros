lista = [50, 75, 46, 22, 80, 65, 8]
mayor = 0
menor = 1000
i = 0
while i<len(lista):
    if lista[i] < menor:
        menor = lista[i]
    if lista[i] > mayor:
        mayor = lista[i]
    i = i + 1
print(menor, mayor)