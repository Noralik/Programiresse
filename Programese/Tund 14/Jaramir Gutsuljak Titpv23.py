import random as r
a = 10
hh = []
for g in range(a):
    Randoms = r.randint(-20, 20)
    hh.append(Randoms)
x = hh
# abs_ll = [abs(x) for x in hh]
help = [x * -1 for x in hh]
print("Original random:", hh)
print("-/+ random:", help)