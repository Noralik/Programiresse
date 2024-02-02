# a=int(100)
# b=float(a)
# d=str(a)
# c=bool(a)
# print (a, b, d, c)
# print(type(a), type(b), type(c), type(d))


#and "логические умножение" 0*0=0	0*1=0	1*0=0	1*1=1
#or "логическое сложение" 0+0=0	0+1=1	1+0=1	1+1=1
# a=float(-0.1)
# b=bool(a)
# print(a, b)
# print(type(a), type(b))

# A=True
# B=False
# C=A and B
# print(C)

# int=(a)
# int=(b)
# int=(c)
# int=(A)
# int=(B)
# int=(C)
# for a=0
#     next for b =1
#         next	A = a
#                 B = b
#                 C = A and B
#                 print("C = A and B")

















































for a in (0, 1):
    for b in (0,1):
        A=bool(a)
        B=bool(b)
        C = A and B
        print (A, " and ",B ,"=", C)