nome = str(input('Digite seu nome :')).strip().title()
if nome=='Klayton':
    print('Que nome bonito !')
elif nome=='Ana' or nome=='Pedro':
    print('Seu nome é bem popular no Brasil !')
else:
    print('Que nome comum !')
print(f'Tenha um bom dia, \033[1;36m{nome}\033[m !')