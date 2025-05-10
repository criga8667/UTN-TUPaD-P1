hemis = input("ingresar en que hemisferio se encuentra (n/s): ")
mes = int(input("ingresar el numero de mes(1 para enero, 2 para febrero): "))
dia = int(input("ingresar que dia es: "))

if hemis == "n" or hemis == "N":
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        esta = "invierno"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        esta = "primavera"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        esta = "verano"
    else:
        esta = "otoño"
elif hemis == "s" or hemis == "S":
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        esta = "verano"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        esta = "otoño"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        esta = "invierno"
    else:
        esta = "primavera"

print(f"En la fecha {dia}/{mes}, en el hemisferio {hemis}, estas en la estacion: {esta}")
