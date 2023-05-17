#Escribir un programa que almacene el abcedario, 
#elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
#y muestre por pantalla la lista resultante.
abc = list("abcdefghijklmnopqrstuvwxyz")
i = len(abc)
while i >= 0:
    if i%3 == 0:
        del abc[i]
    i = i - 1

print(abc)




