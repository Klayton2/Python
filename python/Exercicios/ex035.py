print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
r1 = float(input('Digite o valor de um comprimento de reta :'))
r2 = float(input('Digite o valor de outro comprimento de reta :'))
r3 = float(input('Digite o valor de outro comprimento de reta :'))
lado_maior = r1
lado1 = r2
lado2 = r3
if r2>lado_maior:
    lado_maior = r2
    lado1 = r1
    lado2 = r3
if r3>lado_maior:
    lado_maior = r3
    lado1 = r1
    lado2 = r2
if lado_maior>(lado1 - lado2) and lado_maior<(lado1 + lado2):
    print(f'Os segmentos de reta {r1}, {r2} e {r3} formam um triângulo !')
else:
    print('Os segmentos de reta não formam um triângulo !')
print(lado_maior,lado1,lado2)