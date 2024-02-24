num = int(input("Digite um número (0 a 9999) : "))
un = num % 10
num = (num - un) /10
dz = num % 10
num = (num - dz) / 10
ce = num % 10
num = (num - ce) / 10
mi = num % 10
print(f'O número {num} decomposto fica :\nUnidades : {un:.0f}\nDezenas : {dz:.0f}\nCentenas : {ce:.0f}\nMilhares : {mi:.0f}')