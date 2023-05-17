#Escribir un programa que almacene el abcedario, 
#elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
#y muestre por pantalla la lista resultante.
abc = list("abcdefghijklmnopqrstuvwxyz")
i =0
abc1 = []

while i< len(abc):
    if i%3 != 0:
        abc1.append(abc[i])
    i = i + 1
abc = abc1[:]
print(abc)




