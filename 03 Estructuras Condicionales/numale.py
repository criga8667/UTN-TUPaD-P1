import random
from statistics import mode, median, mean
num_aleatorio = [random.randint(1, 100) for _ in range(50)]
media = mean(num_aleatorio)
mediana = median(num_aleatorio)
moda = mode(num_aleatorio)
print(num_aleatorio)
if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda: 
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")
