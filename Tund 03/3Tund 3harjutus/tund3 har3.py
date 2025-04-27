# maxnum=int(input("How many numbers? "))
# for counter in range (1, maxnum):
#     num=int(input("Number = "))
#     if(counter==1):
#         max=num
#     else:
#         if(num>max):
#             max=num
# print("max =", max)
#         
#         
# 
# max=num
# counter=2
# while(counter<=maxnum):
#    num=int(input("Next number -> "))
#    if(num>max):
#        max=num
#    counter=counter+1
# print("max =", max)
# 
# 
# 
# for counter in (1,5,2,3,4,6,8,7,9,0):
# a=(1,5,2,3,4,6,8,7,9,0)
# for counter in a:
#     print(counter)
# #print(a)
# 
# 
# 
# for counter in range(1,-10,-1):
#     print(counter)









# maxnum=0
# while(maxnum<=0):
#     maxnum=int(input("How many numbers?"))
# for counter in range (1, maxnum):
#     num=int(input("number = "))
#     if(counter==1):
#         max=num
#     else:
#         if(num>max):
#             max=num
# print("max =", max)



#Error="Error"+te

text="How many number?"
maxnum=0
while(maxnum<=0):    
    maxnum=int(input(text))
    text="Error! " +text
for counter in range (1, maxnum):
    num=int(input("number = "))
    if(counter==1): 
        max=num
    else:
        if(num>max):
            max=num
print("max =", max)
