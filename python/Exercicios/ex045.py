from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
pc = randint(0,2)
print('\033[1;36m-=-\033[m'*30)
print('{:^80}'.format('JOKÊNPO'))
print('\033[1;36m-=-\033[m'*30)
print('{:^80}'.format('0 -> Pedra'))
print('{:^80}'.format('1 -> Papel'))
print('{:^80}'.format('2 -> Tesoura'))
print('\033[1;36m-=-\033[m'*30)
jog = int(input('Digite 0-(Pedra),1-(Papel) ou 2-(Tesoura) :'))
print('\033[1;34mJO\033[m')
sleep(1)
print('\033[1;34mKÊN\033[m')
sleep(1)
print('\033[1;34mPO\033[m')
sleep(1)
print('\033[1;36m-=-\033[m'*20)
print(f'\033[1;35mA máquina jogou {itens[pc]}\033[m')
print(f'\033[1;32mVocê jogou {itens[jog]}\033[m')
print('\033[1;36m-=-\033[m'*20)
if pc == 0:
    if jog == 0:
        print('\033[1;33mEmpate!!\033[m')
    elif jog == 1:
        print('\033[1;34mVocê ganhou !!\033[m')
    elif jog == 2:
        print('\033[1;31mVocê perdeu !!\033[m')
    else:
        print('\033[1;31mOpção errada !!!\033[m')
elif pc == 1:
    if jog == 0:
        print('\033[1;31mVocê perdeu !!\033[m')
    elif jog == 1:
        print('\033[1;33mEmpate !!\033[m')
    elif jog == 2:
        print('\033[1;34mVocê ganhou !!\033[m')
    else:
        print('\033[1;31mOpção errada !!!\033[m')
elif pc == 2:
    if jog == 0:
        print('\033[1;32mVocê ganhou!!\033[m')
    elif jog == 1:
        print('\033[1;31mVocê perdeu !!\033[m')
    elif jog == 2:
        print('\033[1;34mEmpate !!\033[m')
    else:
        print('\033[1;31mOpção errada !!!\033[m')