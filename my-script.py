finIntervalo = int(input("Ingrese el numero a evaluar: "))
inicioIntervalo = 0
salida = ""
while (inicioIntervalo <= finIntervalo):
    if( inicioIntervalo % 2 == 0):
        salida = salida + "," + str(inicioIntervalo)
    inicioIntervalo = inicioIntervalo + 1
print(salida)