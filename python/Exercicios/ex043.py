peso = float(input('Informe seu peso :'))
altura = float(input('Informe sua altura : '))
imc = peso / pow(altura,2)
if imc < 18.5:
    print(f'Seu peso é {peso:.1f} kg e sua altura é {altura:.2f} m , seu imc é {imc:.1f} , você está na classe ABAIXO DO PESO !!')
elif imc > 18.5 and imc < 25:
    print(f'Seu peso é {peso:.1f} kg e sua altura é {altura:.2f} m , seu imc é {imc:.1f} , você está na classe PESO IDEAL !!')
elif imc > 25 and imc < 30 :
    print(f'Seu peso é {peso:.1f} kg e sua altura é {altura:.2f} m , seu imc é {imc:.1f} , você está na classe SOBREPESO !!')
elif imc > 30 and imc < 40:
    print(f'Seu peso é {peso:.1f} kg e sua altura é {altura:.2f} m , seu imc é {imc:.1f} , você está na classe OBESIDADE !!')
else:
    print(f'Seu peso é {peso:.1f} kg e sua altura é {altura:.2f} m , seu imc é {imc:.1f} , você está na classe OBESIDADE MÓRBIDA !!')