import matplotlib.pyplot as plt
ent = open("dolar1.txt")
x = []
y = []
for linea in ent:
    linea = linea.rstrip("\n")
    lista = linea.split(" ")
    x.append(lista[0])
    y.append(float(lista[1]))

plt.plot(x, y)
plt.title("Dolar Observado")
plt.show()
