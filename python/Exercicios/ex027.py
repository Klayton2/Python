nome = str(input('Digite seu nome : ')).strip()
div = nome.split()
print(f'Seu nome é {nome}\nPrimeiro nome : {div[0]}\núltimo nome : {nome[len(div)-1]}')