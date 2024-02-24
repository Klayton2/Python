from datetime import date
ano = int(input('Informe seu ano de nascimento :'))
idade = date.today().year - ano
if idade > 20:
    print(f'Sua idade é {idade}, e você pertence a categoria é a MASTER !!')
elif idade > 14 and idade < 19:
    print(f'Sua idade é {idade}, e você pertence a categoria é a JUNIOR !!')
elif idade > 9 and idade < 14:
    print(f'Sua idade é {idade}, e você pertence a categoria é a INFANTIL !!')
elif idade < 9:
    print(f'Sua idade é {idade}, e você pertence a categoria é a MIRIM !!')
else:
    print(f'Sua idade é {idade}, e você pertence a categoria é a SÊNIOR !!')