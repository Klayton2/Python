s = float(input('Informe seu salário :'))
if s>1250:
    sn = s + (s*0.10)
    print(f'Seu salário antigo é R$ {s:.2f}, depois do aumento de 10% ficou R$ {sn:.2f} .')
else:
    sn = s + (s*0.15)
    print(f'Seu salário antigo é R$ {s:.2f}, depois do aumento de 15% ficou R$ {sn:.2f} .')