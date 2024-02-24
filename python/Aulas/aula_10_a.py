n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a primeira nota : '))
m = (n1+n2)/2
if m>=7:
    print(f'Sua média foi {m:.1f} e você foi aprovado !')
else:
    print(f'Sua média foi {m:.1} e você foi reprovado !')