def es_primo(numero):
    li = 2
    lf = int(numero/2 + 1)
    estado = True
    divisor = li
    while divisor <= lf:
        print(divisor)
        if numero%divisor == 0:
            estado = False
        divisor = divisor + 1
    return estado

numero = int(input("Numero: "))
print(es_primo(numero))
