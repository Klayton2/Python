n1 = int(input('Digite um número :'))
n2 = int(input('Digite outro número :'))
n3 = int(input('Digite outro número :'))
max = n1
min = n1
#Verificando o maior número
if n2>max:
    max = n2
if n3>max:
    max = n3
print(f'O maior valor é {max} .')
#Verificando o menor número
if n2<min:
    min = n2
if n3<min:
    min = n3
print(f'O menor valor é {min} .')