from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em númeor entre 0 .. 5 . Tente adivinhar ....') # computador vai sortear os números
print('-=-'*20)
jog = int(input('Tente adivihar um número : ')) # jogador tenta adivinhar
print('-=-'*20)
print('PROCESSANDO....')
sleep(3)
pc = randint(0,5)
if jog==pc:
    print('Você acertou ,parábens !')
else:
    print(f'Você errou ! O número certo é {pc}')

