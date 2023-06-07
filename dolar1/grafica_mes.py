import matplotlib.pyplot as plt

def calcula_promedio(mes, nro):
    suma = 0
    cont = 0
    for elem in mes:
        ms = elem[0:2]
        va = float(elem[2:])
        if ms == nro:
            suma = suma + va
            cont = cont + 1
    promedio = suma / cont
    return promedio

ent = open("datos_proc.txt")
mes = []
for linea in ent:
    linea = linea.rstrip("\n")
    lista = linea.split(" ")
    fecha = lista[0]
    valor = lista[1]
    nombre = ['ene','feb','mar','abr','may','jun']
    l_fecha = fecha.split(".")
    if l_fecha[1] == 'ene':
        nro = "01"
    if l_fecha[1] == 'feb':
        nro = "02"
    if l_fecha[1] == 'mar':
        nro = "03"
    if l_fecha[1] == 'abr':
        nro = "04"
    if l_fecha[1] == 'may':
        nro = "05"
    if l_fecha[1] == 'jun':
        nro = "06"
    mes.append(nro+valor)
ent.close()
# Procesar
lista_meses = []
meses = ["01","02","03","04", "05","06"]
for i in meses:
    promedio = calcula_promedio(mes, i)
    lista_meses.append(promedio)
plt.plot(lista_meses)
plt.show()



       
    