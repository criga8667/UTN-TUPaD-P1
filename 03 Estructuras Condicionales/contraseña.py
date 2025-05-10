cont = input("ingrese una contraseña entre 8 y 14 caracteres: ")
if len(cont) <= 8 or len(cont) >= 14:
    print("ingreso una contraseña correcta")
else:
    print("por favor ingrese una contraseña entre 8 y 14 caracteres")