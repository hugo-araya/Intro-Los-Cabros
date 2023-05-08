import os
if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')
maes = input("Clave maestra: ")
clave1 = ''
clave2 = ''
i = 0
while i < len(maes):
    if int(maes[i])%2 == 0:
        clave2 = clave2 + maes[i]
    else:
        clave1 = clave1 + maes[i]
    i = i + 1
print("Clave 1: ", clave1)
print("Clave 2: ", clave2)   
    

