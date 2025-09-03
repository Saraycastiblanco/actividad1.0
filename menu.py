#saray#
import math
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print("Menú de operaciones: suma, resta, multiplicación, división, raíz, porcentaje")
operador = input("Elige una operación: ")

if operador == "suma":
    resultado = num1 + num2

elif operador == "resta":
    resultado = num1 - num2

elif operador == "multiplicacion":
    resultado = num1 * num2

elif operador == "division":
    resultado = num1 / num2

elif operador == 'raíz':
    resultado = f"Raíz de {num1}: {math.sqrt(num1)}\nRaíz de {num2}: {math.sqrt(num2)}"
elif operador == 'porcentaje':
    resultado = (num1 * num2) / 100
print("El resultado es", resultado)