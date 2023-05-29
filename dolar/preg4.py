ent = open("dolar1.txt")
for linea in ent:
    linea = linea.rstrip("\n")
    lista = linea.split(" ")
    valor = float(lista[1])
    lista1 = lista[0].split("-")
    dia = lista1[0]
    mes = lista1[1]
    agno = lista1[2]
    month = "ene"
    suma = 0
    while month == mes:
        suma = suma + valor
        linea = ent.readline()
        linea = linea.rstrip("\n")
        lista = linea.split(" ")
        valor = float(lista[1])
        lista1 = lista[0].split("-")
        dia = lista1[0]
        mes = lista1[1]
        agno = lista1[2]
    print(suma)
    month = mes
    


