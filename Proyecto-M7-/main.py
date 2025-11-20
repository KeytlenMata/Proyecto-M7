# main.py

import Operaciones

# Bienvenida y explicación
print("=" * 60)
print("    🔢 BIENVENIDO A LA CALCULADORA BÁSICA EN PYTHON 🔢")
print("=" * 60)
print("Este programa te permite realizar operaciones")
print("matemáticas simples: suma, resta, multiplicación")
print("y división entre dos números.")
print("-" * 60)

# Solicitar los dos números
try:
    num1 = float(input(" --> Ingresa el primer número: "))
    num2 = float(input(" --> Ingresa el segundo número: "))
except ValueError:
    print("\n❌ Error: Por favor, ingresa valores numéricos válidos.")
    exit()

# Mostrar menú de operaciones
print("\n" + "=" * 60)
print("🧮 MENÚ DE OPERACIONES DISPONIBLES")
print("=" * 60)
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("-" * 60)

# Pedir la opción hasta que sea válida
opcion = None
while opcion not in ["1", "2", "3", "4"]:
    opcion = input("--> Elige una opción (1-4): ")
    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida. Por favor, selecciona un número del 1 al 4 ⚠️")

# Ejecutar la operación seleccionada (ahora sabemos que es válida)
if opcion == "1":
    resultado = Operaciones.sumar(num1, num2)
    operacion = "suma"
elif opcion == "2":
    resultado = Operaciones.restar(num1, num2)
    operacion = "resta"
elif opcion == "3":
    resultado = Operaciones.multiplicar(num1, num2)
    operacion = "multiplicación"
elif opcion == "4":
    resultado = Operaciones.dividir(num1, num2)
    operacion = "división"

# Mostrar el resultado con formato
print("\n" + "=" * 60)
print(f"✅ Resultado de la {operacion}: {resultado}")
print("-" * 60)

# Mensaje de despedida
print("\n ¡Gracias por usar la calculadora!, hasta luego.👋")
print("=" * 60)