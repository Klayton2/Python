vi = float(input('Informe o valor do imóvel selecinado : R$ '))
s = float(input('Informe seu salário : R$ '))
a = float(input('Informe o tempo para quitação do empréstimo :'))
np = a * 12
p = vi / np
if p<=(s-(s*0.3)):
    print('-=-'*50)
    print('Parabéns seu empréstimo foi \033[1;34maprovado\033[m !')
    print('-=-'*50)
else:
    print('-=-'*40)
    print('Infelizmente as parcelas do empréstimo ultrapassaram 30% do seu salário , por isso seu empréstimo foi \033[1;31mnegado\033[m !')
    print('-=-'*40)
print(f'O imóvel selecinado foi R$ {vi:.2f}, seu salário atual é R$ {s:.2f} e deseja finalizar a quitação do empréstimo em {a} anos.\nVocê pagará {np:.0f} parcelas de R$ {p:.2f}.')