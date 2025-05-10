palabra = input("Ingrese una frase o palabra: ")
ult_letra = palabra[-1]
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

if ult_letra in vocales:
    palabra += "!"
    
print(palabra)