l1 = float(input('Digite o valor do 1° lado :'))
l2 = float(input('Digite o valor do 2° lado :'))
l3 = float(input('Digite o valor do 3° lado :'))
if l1 < (l2+l3) and l2 < (l1+l3) and l3 < (l1+l2):
    print(f'Os valores {l1:.1f}, {l2:.1f} e {l3:.1f} formam um triângulo ',end='')
    if l1==l2 and l2==l3 :
        print('EQUILÁTERO !!!')
    elif l1==l2 or l2==l3 or l3==l1:
        print('ISÓCELES !!!')
    else:
        print('ESCALENO !!!')
else:
    print(f'Os valores {l1:.1f}, {l2:.1f} e {l3:.1f} não formam um triângulo !!!')