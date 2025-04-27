# Howmuch = int(input("How much +/-: "))
# YourBalance = int(input("Your Balance: "))
# KKK = int(input("1 / 2 "))

class BankAccount:

    def __init__(self,number,sum):
        self.number = number
        self.balance = sum
        self.lock = False
        
    def  pinInput(self, pin):
        i = 0
        while i<3:
            userInput = input("Sisesta parooli: ")
            i+=1
            if pin == userInput:
                lock = False
                print("Õigus parroli")
                break
            else:
                print("Parolli halb")
            if i == 3:
                self.lock = True
                print("te olete blookeritud", self.lock)

    def addMoney(self,sum):
        if self.lock == True:
            print("error your are bloked")
        else:
            self.balance += sum
            print("oli lisatud raha: ", sum)
            print(self.balance)

    def võtanMoney(self,sum):
        if self.lock == True:
            print("error your are bloked")
        else:
            self.balance -= sum
            if sum <=self.balance:
                self.balance -= sum
                print("Success")
                print(self.balance)
            else:
                print("Error")
                print("võtan raha: ", sum)
        
    def control(self):
        KKK = int(input("1 / 2 "))
        if KKK==1:
            O = self.addMoney(int(input("How much? ")))
        else:
            P = self.võtanMoney(int(input("How much? ")))

acc1 = BankAccount("123456789", int(input("Your Balance1: "))) # balance
acc1.pinInput("1122")
acc2 = BankAccount("123456789", int(input("Your Balance2: "))) # balance
acc1.pinInput("1122")

acc1.control()
acc2.control()