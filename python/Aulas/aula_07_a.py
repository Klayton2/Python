n1 = int(input("Digite um número :"))
n2 = int(input("Digite um número :"))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma vale {} ,a multiplicação vale {} , a divisão  vale {:.3f}".format(s, m , d), end=", ")
print("A divisão inteira vale {} e a exponênciação vale {}.".format(di ,e))