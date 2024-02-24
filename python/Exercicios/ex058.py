from random import randint
print('Vou pensar em número de 0 até 5, tente adivinhar !!!')
jog = int(input('Tente adivinhar o número :'))
pc = randint(0,5)
qtd = 1
while jog != pc:
    print('Vou pensar em número de 1 até 5, tente adivinhar !!!')
    jog = int(input('Você errou !!! Tente adivinhar o número :'))
    if jog != pc:
        qtd +=1
if jog == pc:
    print(f'Você digitou o número {jog} , meus parabéns você ganhou na {qtd+1}° tentativa')

