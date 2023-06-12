def valida1(direc):
    i = 0
    largo = len(direc)
    cont = 0
    mensaje = "NO VALIDO"
    while i < largo:
        if direc[i] == '@':
            mensaje = "VALIDO"
            cont = cont + 1
        i = i +1
    if cont == 1:
        mensaje
    else:
        return "NO VALIDO"

def valida2(direc):
    contador = direc.count('@')
    if contador == 1:
        mensaje = "VALIDO"
    else:
        mensaje = "NO VALIDO"
    return mensaje

def valida3(direc):
    if "@" in direc:
        mensaje = "VALIDO"
    else:
        mensaje = "NO VALIDO"
    return mensaje

direccion = input("Ingrse su e-mail: ")
estado = valida3(direccion)
print(estado)
