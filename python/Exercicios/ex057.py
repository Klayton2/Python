sexo = str(input('Digite seu sexo (F/M) :')).strip().upper()
if sexo != 'F' and sexo != 'M':
    print('Sexo inválido\n')
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo (F/M) :')).upper().strip()
    if sexo != 'F' and sexo != 'M':
        print('Sexo inválido\n')