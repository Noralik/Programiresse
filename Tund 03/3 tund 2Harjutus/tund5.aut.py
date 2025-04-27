maxnum=int(input("How many numbers? "))
num=int(input("First number -> "))
max=num
counter=2
while(counter<=maxnum):
    num=int(input("Next number -> "))
    if(num>max):
        max=num
    counter=counter+1
print("max =", max)