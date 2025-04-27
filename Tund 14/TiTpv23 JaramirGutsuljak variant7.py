import math

y = int(input("Ввежите Y: "))
M = int(input("Ввежите M: "))

N = (M**2+2.8*M+0.355)/(math.cos(2*y)+3.6)
u = (math.cos(2*y)+3.6)



if u==0:
    print("Error")
else:
    print(N)
    
print("Формула: (M**2+2.8*M+0.355)/(math.cos(2*y)+3.6)")