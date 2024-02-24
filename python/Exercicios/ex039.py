from datetime import date
ano = int(input('Informe seu o ano de nascimento :'))
at = date.today().year
idade = (at-ano)
rest = idade
if (rest-18) < 0:
    rest = idade - 18
    rest = rest*-1
elif (rest-18) > 0:
    rest = idade - 18

if (at-ano) < 18:
    print(f'Você tem {idade} anos, você ainda tem {rest} anos para se alistar nas forças armadas !!')
elif (at-ano) == 18:

    print(f'Você tem {idade} anos, agora é hora de se alistar nas forças armadas !!')
else:
    print(f'Você tem {idade} anos, seu tempo de alistamento militar se expirou à {rest} anos !!')
