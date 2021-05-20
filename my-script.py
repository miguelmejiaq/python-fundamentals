# finIntervalo = int(input("Ingrese el numero a evaluar: "))
# inicioIntervalo = 0
# salida = ""
# while (inicioIntervalo <= finIntervalo):
#     if( inicioIntervalo % 2 == 0):
#         salida = salida + "," + str(inicioIntervalo)
#     inicioIntervalo = inicioIntervalo + 1
# print(salida)

### Solución
# plantillas de texto.
# var_PreguntaNumero = 'Ingrese el {valor} numero: '
# var_preguntaNombre = 'Ingrese su nombre: '
# var_textoNumero1, var_textoNumero2 = 'primer','segundo'
# # Definimos las entradas
# var_numero1 = int(input(var_PreguntaNumero.format(valor = var_textoNumero1)))
# var_numero2 = int(input(var_PreguntaNumero.format(valor = var_textoNumero2)))
# var_nombre = input(var_preguntaNombre)
# # Salidas
# print("el promedio es: ",(var_numero1 + var_numero2) // 2)
# print("la suma de los 2 números es: ",var_numero1 + var_numero2)
# print("El cuadrado del primer número es: ",pow(var_numero1,2),"El cuadrado del segundo número es: ", var_numero2**2)
# print("Nombre en mayuscula: ",var_nombre.upper())
# print(var_nombre.lower().replace("i","*").title())
# print(var_nombre*3)

print("Comienzo")
for i in range(3):
    print(i, "Hola ", end="")
    print()
    print("FIN DE LA CORRIDA")