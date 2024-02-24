from math import hypot
catop = float(input('Informe o valor do cateto oposto : '))
catad = float(input('Informe o valor do cateto adjacente : '))
print(f'Um triângulo de dimensões {catop}x{catad} possui a hipotenusa de valor {hypot(catop,catad):.2f}')