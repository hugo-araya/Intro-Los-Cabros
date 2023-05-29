# QUiero saber la fecha del mayor valor
ent = open("dolar1.txt")
mayor = 0
for linea in ent:
    linea = linea.rstrip("\n")
    lista = linea.split(" ")
    if mayor < float(lista[1]):
        mayor = float(lista[1])
        fecha = lista[0]
ent.close()
print(fecha)
