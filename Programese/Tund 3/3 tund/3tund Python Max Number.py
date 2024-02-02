number1=int(input("First Number: "))
number2=int(input("Second Number: "))
number3=int(input("Third Number: "))
#обозначает цисла1 2 3
max=number1
if(number2>max):
    max=number2
if(number3>max):
    max=number3
print(f"max= {max} from {number1}, {number2} and {number3}")
# программа говорит что за 1=n 2=n 3=n