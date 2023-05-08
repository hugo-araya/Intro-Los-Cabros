import os
if os.name == 'posix':
    os.system('clear')
else:
    os.system('cls')
print(os.listdir())
pal1 = input("Palabra 1: ")
pal2 = input("Palabra 2: ")
largo1 = len(pal1)
largo2 = len(pal2)
ult1 = pal1[largo1-3:]
ult2 = pal2[largo2-3:]
if ult1 == ult2:
    print("Riman")
else:
    ult1 = pal1[largo1-2:]
    ult2 = pal2[largo2-2:]
    if ult1 == ult2:
        print("Riman poco")
    else:
        print("No riman")
