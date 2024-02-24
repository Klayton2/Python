vel = int(input('Informe a velocidade do carro :'))
if vel>80:
    mul = (vel-80)*7
    print(f'A velocidade do carro é {vel} km/h ,você foi multado em R$ {mul:.2f} .')
print('Tenha um bom dia e dirija com segurança .')