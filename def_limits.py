from sympy import *
import matplotlib

init_printing()

# define x e y como variaveis simbolicas
var('x,y')
f = Lambda(x, (x ** 3 - 3 * x + 2) * exp(-x / 4) - 1)
print(f)
limit(abs(x) / x, x, 0)
limit(abs(x) / x, x, 0, '-')
limit(abs(x) / x, x, 0)
limit(abs(x) / x, x, 0, '-')
limit(f(x), x, oo)
limit(f(x), x, -oo)
nsolve(f(x), x, 46)

print()

#plot(f(x), (x, 40, 50))
