def genera_alfabeto():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ini = 65
    lista = []
    for letra in letras:
        lis = [letra, ini]
        lista.append(lis)
        ini = ini + 1
    numeros = "0123456789"
    ini = 48
    for nume in numeros:
        lis = [nume, ini]
        lista.append(lis)
        ini = ini + 1
    lista.append(["!", 33])
    lista.append([",", 44])   
    lista.append([".", 46]) 
    lista.append([":", 58])   
    lista.append([";", 59])    
    lista.append(["?", 63])  
    lista.append([".", 45])        
    return lista


print(genera_alfabeto())


    