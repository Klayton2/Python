distancia = float(input('Informe a distância da viagem em km :'))
if distancia>200:
    preco = distancia * 0.45
    print(f'Sua viagem será de {distancia:.2f} km e custará R$ {preco:.2f} .')
else:
    preco = distancia * 0.5
    print(f'Sua viagem será de {distancia:.2f} km e custará R$ {preco:.2f} .')