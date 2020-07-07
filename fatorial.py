def fat(n):	
	    resultado = 1
	    while n > 0:
	        resultado = resultado * n
	        n = n - 1
	    return resultado

print("Entre com o numero: ")
num=int(input())
	
print("Fatorial de ", num, " igual a:", fat(num))
