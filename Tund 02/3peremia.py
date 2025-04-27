number1=int(input("First number: "))
number2=int(input("second number: "))
number3=int(input("third number: "))

if (number1>number2) :
    if(number1>number3) :
        max=number1
    else:
        max=number3
else:
    if(number2>number3) :
        max=number2
    else:
        max=number3
print("maximum = ", max)




