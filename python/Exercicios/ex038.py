n1 = float(input('Digite um número qualquer :'))
n2 = float(input('Digite um número qualquer :'))
if n1 > n2:
    print(f'Entre os números {n1} e {n2} , o maior é {n1} .')
elif n2 > n1:
    print(f'Entre os números {n1} e {n2} , o maior é {n2} .')
else:
    print(f'Os números {n1} e {n2} são iguais.')