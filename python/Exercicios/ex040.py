n1 = float(input('Informe a 1° nota :'))
n2 = float(input('Informe a 2° nota :'))
m = (n1+n2)/2
if m > 7:
    print(f'Suas notas foram {n1:.1f} e {n2:.1f} respectativamente e sua média foi {m:.1f}, MEUS PARABÉNS VOCÊ FOI APROVADO !!')
elif m < 5:
    print(f'Suas notas foram {n1:.1f} e {n2:.1f} respectativamente e sua média foi {m:.1f}, INFELIZMENTE VOCÊ FOI REPROVADO !!')
else:
    print(f'Suas notas foram {n1:.1f} e {n2:.1f} respectativamente e sua média foi {m:.1f}, SE ESFORCE MAIS DA PRÓXIMA VEZ, VOCÊ ESTÁ DE RECUPERAÇÃO !!')