#Ejercicio 1
print("hola mundo!")

#Ejercicio 2
nombre = input("ingrese su nombre: ")
print(f"hola {nombre}!")

#Ejercicio 3
nombre1 = input("ingrese su nombre: ")
apellido = input(f"ingresa tu apellido {nombre1}: ")
edad = input(f"ingresa tu edad {nombre1}: ")
pais = input(f"de que pais sos:")
print(f"soy {nombre1} {apellido}, tengo {edad} años y vivo en {pais} ")

#Ejercicio 4
radio = float(input("ingrese el radio del ciculo: "))
area =  3.14 * radio**2
perimetro = 2 * 3.14 * radio
print (f"el area del ciculo es: {area} y el perimetro es : {perimetro}")

#Ejercicio 5
segundos = int(input("ingrese la cantidad de segundos: "))
horas = segundos // 3600
print(f"la cantidad de horas son: {horas}")

#Ejercicio 6
numero3 = int(input("ingrese el numero del que quiere su tabla de multiplicar: "))
for i in range(1,11):
    print(f"{numero3} x {i}: {numero3*i}")

#Ejercicio 7
numero4 = int(input("ingrese el primer numero: "))
numero5 = int(input("ingrese el segundo numero: "))
print(f"la suma de los 2 numeros es: {numero4 + numero5}")
print(f"la resta de los 2 numeros es: {numero4 - numero5}")
print(f"la multiplicacion de los 2 numeros es: {numero4 * numero5}")
print(f"la division de los 2 numeros es: {numero4 / numero5}")

#Ejercicio 8
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)  # Fórmula del IMC
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#Ejercicio 9
celcius = float(input("ingrese la temperatura a convertir: "))
fahre = celcius * 9/5 + 32
print(f"la tempertura en fahrenheit es: {fahre:.2f}")

#Ejercicio 10
numero6 = float(input("ingrese el primer numero: "))
numero7 = float(input("ingrese el segundo numero: "))
numero8 = float(input("ingrese el tercer numero: "))
promedio = (numero6 + numero7 +numero8) / 3
print(f"el promedio de los tres numeros es: {promedio:.2f}")