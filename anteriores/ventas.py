sueldo_base = int(input('Sueldo base:'))
v1 = int(input('Venta 1: '))
v2 = int(input('Venta 2: '))
v3 = int(input('Venta 3: '))
ventas = v1 + v2 + v3
comision = ventas * 0.1
sueldo_recibir = sueldo_base + comision
print('Comisio: ', comision)
print('Sueldo a recibir: ', sueldo_recibir)
