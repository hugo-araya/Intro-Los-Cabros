ent = open("datos_proc.txt")
cont = 0
suma = 0
mayor = -1
for linea in ent:
    linea = linea.rstrip("\n")
    lista = linea.split(" ")
    fecha = lista[0]
    valor = float(lista[1])
    suma = suma + valor
    cont = cont + 1
    if valor > mayor:
        mayor = valor
        fecha_mayor = fecha
ent.close()
print(fecha_mayor, mayor)
promedio = suma / cont
print(promedio)

