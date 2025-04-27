Nimi1 = input("What is your name?")
a = int(input("Your age: "))

Nimi2 = input("What is your name?")
b = int(input("Your age: "))

Nimi3 = input("What is your name?")
c = int(input("Your age: "))

Nimi4 = input("What is your name?")
d = int(input("Your age: "))


class Proverka:
    def __init__(self, vanus, nimi):
        self.vanus = vanus
        self.nimi = nimi
        
    def  proverVan(self):
        print(self.vanus)
        if int(self.vanus)>= 18 :
            print("proshol")
        else:
            print("Ne proshol")

Nimi1 = Proverka(a, Nimi1)
Nimi2 = Proverka(b, Nimi2)
Nimi3 = Proverka(c, Nimi3)
Nimi4 = Proverka(d, Nimi4)

Nimi1.proverVan()
Nimi2.proverVan()
Nimi3.proverVan()
Nimi4.proverVan()
#proverVan