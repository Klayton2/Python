nome = str(input('Digite seu nome : ')).strip()
dividido = nome.split()
print(f'seu nome é {nome}\nseu nome com as letras maiúsculo {nome.upper()}\nseu nome com letra minúsculas {nome.lower()}\nseu nome possui {len(nome.replace(" ",""))} caracteres', end ="\n")
print(f'seu primeiro nome é {dividido[0]} possui {len(dividido[0])} caracteres.')