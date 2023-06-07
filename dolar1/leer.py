ent = open("datos.txt")
sal = open("datos_proc.txt", "w")
for linea in ent:
    linea = linea.rstrip("\n")
    lista = linea.split("\t")
    fecha = lista[0]
    valor = lista[1]
    if valor != '':
        valor = valor.replace(",", ".")
        sal.write(fecha + " " + valor + "\n")
ent.close()
sal.close()

    
    




