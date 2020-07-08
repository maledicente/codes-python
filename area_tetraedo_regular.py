#CALCULANDO A AREA DE UM TETRAEDO REGULAR

#altura de um tetraedro: h=(a*stqr(6))/3
# a= aresta do tetraedro

aresta=float(input("Entre com valor da aresta(metros): "))
sb=float(input("Entre com valor da base do tetraedro(metros): "))
                   
def h_tetraedro(x):
   if x < 0:
      print("Valor invalido para aresta")
   else:
      return (x*pow(6,1/2))/3

def b_tetraedro(a):
   if a < 0:
      print("Valor invalido para base do tetraedro")
   else:
      return (pow(a,2) * pow(3,1/2))/4
   
#volume do tetraedro: v=1/3*Sb*h
def v_tetraedo():
   volume = 1/3 * b_tetraedro(sb) * h_tetraedro(aresta)
   print("O volume do tetraedro e: {:.2f}m2".format(volume))


v_tetraedo()



   
