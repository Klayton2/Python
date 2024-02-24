from math import sin, cos,tan,radians

ang = float(input('Informe um ângulo :'))
print(f'O ângulo {ang}°\ntem o seno igual a {sin(radians(ang)):.2f}°\ntem o cosseno igual a {cos(radians(ang)):.2f}°\ne tem a tangente igual a {tan(radians(ang)):.2f}°')