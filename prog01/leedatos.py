datos = open('datos.txt')
for linea in datos:
    linea = linea.rstrip('\n')
    lista = linea.split(',')
    if lista[2] == 'Talca':
        talca = lista[:]
datos.close()
print(talca)




