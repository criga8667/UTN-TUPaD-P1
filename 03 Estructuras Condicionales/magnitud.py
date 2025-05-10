mag = int(input("ingrese la magniturd del terremoto: "))
if mag >= 7:
    print("extremo")
elif mag >= 6:
    print("muy fuerte")
elif mag >= 5:
    print("fuerte")
elif mag >= 4:
    print("moderado")
elif mag >= 3:
    print("leve")
else:
    print("muy leve")