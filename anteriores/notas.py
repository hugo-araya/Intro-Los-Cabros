nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))

examen = float(input('Examen: '))
trabajo = float(input('Trabajo: '))

notas =(nota1 + nota2 + nota3)/3

final = notas*0.55 + examen*0.3 + trabajo*0.15

print("La nota final es: ", final)

if final >= 4:
    print('Aprobado')
    if final == 4:
        print(' -------> Gracias profesor')
else:
    print('Reprobado')
    if final == 3.9:
        print(' ------ > Casi casi')
print('Eso es todo')
