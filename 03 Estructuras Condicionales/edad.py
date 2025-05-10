edad = int(input("ingrese su edad: "))
if edad < 12:
    print("es un niño/a")
elif edad < 18:
    print("es un adolecente")
elif edad < 30:
    print("adulto/a joven")
else:
    print("adulto/a")
