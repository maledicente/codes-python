numero = int(input("Digite um numero (0 >): "))
if numero == 0:
	print("Numero invalido")

divisores = 0
for divisor in range(1, numero):
    if numero % divisor == 0:
        divisores = divisores + 1
        if divisores > 1:
          break
if divisores > 1:
  print("O numero {} não é primo".format(numero))
else:
  print("O numero {} é primo.".format(numero))
