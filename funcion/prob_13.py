def generar_n_caracteres(numero, carac):
    return carac * numero

nume = int(input('Numero: '))
cara = input("Caracter: ")
resultado = generar_n_caracteres(nume, cara)
print(resultado)
