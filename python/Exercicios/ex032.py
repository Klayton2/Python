from calendar import isleap
from datetime import date
ano = int(input('Digite um ano para ser analisado ou digite 0 para analisar o ano atual :'))
if ano==0:
    ano = date.today().year
bissexto = isleap(ano)
if bissexto==True:
    print(f'O ano {ano} é bissexto !')
else:
    print(f'O ano {ano} não é bissexto !')

