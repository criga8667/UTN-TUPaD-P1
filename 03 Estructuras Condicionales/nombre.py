nom = input("ingrese su nombre: ")
opc = int(input("1. Si quiere su nombre en mayúsculas\n2. Si quiere su nombre en minúsculas\n3. Si quiere su nombre con la primera letra mayúscula\n"))
if opc == 1:
    print(nom.upper())
elif opc == 2:
    print(nom.lower())
elif opc == 3:
    print(nom.title())