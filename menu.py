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
