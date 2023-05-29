# QUiero saber la fecha del menor valor
ent = open("dolar1.txt")
menor = 100000
for linea in ent:
    linea = linea.rstrip("\n")
    lista = linea.split(" ")
    if menor > float(lista[1]):
        menor = float(lista[1])
        fecha = lista[0]
ent.close()
print(fecha, menor)
