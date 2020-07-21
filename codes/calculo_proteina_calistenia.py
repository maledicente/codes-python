#Numero de gramas de proteina necessarios por dia.

peso = float(input('Entre com seu peso(kg): '))
#0,8 ~> sedentário (quem não pratica nenhum esporte);
#1,0 ~> atleta esporádico (só pratica esportes nos finais de semana);
#1,0 a 1,6 ~> resistência (para quem pratica maratonas, ciclismo ou triátlon);
#1,4 a 1,7 ~> mistos (para quem joga futebol, basquete, vôlei);
#1,6  a 2,0 ~> força (praticantes de musculação, crossfit, fisiculturismo).
print('Voce precisa consumir: {:.2f} gramas de proteina por dia.'.format(peso*1.5))