def generar_n_caracteres(numero, carac):
    return carac * numero

lista = [4, 9, 7]
for nume in lista:
    resultado = generar_n_caracteres(nume, '*')
    print(resultado)

