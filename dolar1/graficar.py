import matplotlib.pyplot as plt
X = []
Y = []
ent = open("datos_proc.txt")
for linea in ent:
    linea = linea.rstrip("\n")
    lista = linea.split(" ")
    fecha = lista[0]
    valor = float(lista[1])
    X.append(fecha)
    Y.append(valor)
ent.close()
plt.title("Valor del dolar")
plt.plot(Y)
plt.show()


