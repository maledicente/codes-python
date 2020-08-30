def euler(x):
   return (1+1/x)**x

for i in range(10):
   print(euler(10**i))