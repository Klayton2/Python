print('-=-'*30)
print('{:^80}'.format('LOJAS SOUSA'))
print('-=-'*30)
valor = float(input('Informe o valor do produto :'))
print('{:^80}'.format('\nFormas de pagamento'))
print(' 1 -> À vista (Dinheiro ou cheque) -> 10% de desconto')
print(' 2 -> À vista (cartão) -> 5% de desconto')
print(' 3 -> Dividido em até 2x -> preço normal')
print(' 4 -> Dividido em 3x ou mais -> 20% de juros')
print('-=-'*30)
forma = int(input('Informe a forma de pagamento :'))
if forma==1:
    valorp = valor - (valor*0.10)
elif forma==2:
    valorp = valor - (valor * 0.05)
elif forma==3:
    p = int(input('Digite a quantidade de parcelas :'))
    valorp = valor
    print(f'Você irá pagar em {p}x de R$ {valorp / p} . ')
elif forma==4:
    p = int(input('Digite a quantidade de parcelas :'))
    valorp = valor + (valor * 0.20)
    print(f'Você irá pagar em {p}x de R$ {valorp / p} . ')
else:
    print('Forma de pagamento inválida !!')
print(f'O produto custa R$ {valor:.2f} , após a ecolha de pagamento você irá pagar R$ {valorp:.2f} .')
