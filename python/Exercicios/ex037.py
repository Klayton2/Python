n = int(input('Digite um número inteiro :'))
print('-=-'*20)
print('        Conversor de bases númericas       ')
print('-=-'*20)
print('     1 ->  Binário        ')
print('     2 ->  Octal          ')
print('     3 ->  Hexadecimal    ')
print('-=-'*20)
op = int(input('Escolha a base númerica :'))
if op == 1:
    print(f'{n} convertido para binário é igual a {bin(n)[2:]} .')
elif op == 2:
    print((f'{n} convertido para octal é igual a {oct(n)[2:]} .'))
elif op == 3:
    print((f'{n} convertido para hexadecimal é igual a {hex(n)[2:]} .'))
else:
    print('Opção inválida !!')