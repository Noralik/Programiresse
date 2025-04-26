# with open("DEEB.txt", "r") as deeb:
#     rida=deeb.readline()
#     sone=rida.replace("\n", "")
#     muutujad=sone.split(";")
#     print(muutujad[0])
    
    

# def deep(k, x, y0):
#     y=k*x+y0
#     return (y)
# Y= deep(3, 6, 9)
# print(Y)


# with open("DEEP.txt", "r") as deep:
#     rida=deep.readline()
#     sone=rida.replace("\n", "")
#     muutujad=sone.split(";")
#     print(muutujad)
#     print(sone)
#     print(rida)
    

# for i in range(5):
#     element = input("элемент списка")
#     deep.append(element)
# print(deep)





# with open("DEEP.txt", "r") as deep:
#      for line in deep:
#          print(line)

def linear(k, x, y0):
    k=float(k); x=float(x); y0=float(y0)
    y=k*x+y0
    print(f"{k} * {x} + {y0} = {y}")
    #1 считывать все строки
with open("DEEP.txt", "r") as deep:
     for line in deep:
         sone=line.replace("\n", "")
         muutujad=sone.split(";")
         print(muutujad)
         linear(muutujad[0], muutujad[1], muutujad[2])
    #2 преобразует список и считывает числа
