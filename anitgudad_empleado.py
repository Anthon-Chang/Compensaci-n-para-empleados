

print("--------GRACIAS POR SUS SERVICIOS DURATE TODO ESTE AÑO--------")

antiguedad = int(input("Ingrese cuantos años a paso en la empresa: "))


if 1 <= antiguedad <= 5:
    bono = antiguedad * 100
elif antiguedad > 5:
    bono = 1000
else:
    bono = 0


print("El bono que recibirá el empleado es:", bono)

print("---------MUCHAS GRACIAS POR SU TRABAJO---------")
