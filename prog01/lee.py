archivo = open('archi.txt')
for linea in archivo:
    linea = linea.rstrip('\n')
    print(linea)