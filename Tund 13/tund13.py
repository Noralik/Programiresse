# mak = [1, 2, 3, 4, 5]
# reverse_mak = sorted(reverse_mak=True)
# print(reverse_mak)
import random as r

Mok = [1, 2, 3, 4, 5]
print("Original Mok ", Mok)
#Обычные принт списка

reverse = Mok [::-1]
print ("reverse Mok ", reverse)
#принт задом наперед реверс

r.shuffle (Mok)
print("random ", Mok)
# принт рандомно ставляющий "цифры/слова"

sortedd = sorted (Mok)
print("Возрастанию ", sortedd)
# принт списка по ворзрастанию

list_desc = sorted (Mok, reverse=True)
print("Убыванию ", Mok)
#принт списка по убыванию



# rr = [0, 1, 2, 3, 4]
# # RR = [4, 3, 2, 1, 0]
# RR = [0]*5
# RR[4] = rr[0]
# RR[3] = rr[1]
# RR[2] = rr[2]
# RR[1] = rr[3]
# RR[0] = rr[4]
# 
# N = len (RR)
# for i in range (0 , N):
#     RR[N-i-1] = rr[i]
# print(rr),print(RR)
# 
# while len (RR)<N:
#     RR[n-i-1]=rr[i]
# print(rr), print(RR)



# rr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # RR = [4, 3, 2, 1, 0]
# RR = [0]*len(rr)
# RR[9] = rr[0]
# RR[8] = rr[1]
# RR[7] = rr[2]
# RR[6] = rr[3]
# RR[5] = rr[4]
# RR[4] = rr[5]
# RR[3] = rr[6]
# RR[2] = rr[7]
# RR[1] = rr[8]
# RR[0] = rr[9]
# 
# N = len (RR)
# for i in range (0 , N):
#     RR[N-i-1] = rr[i]
# print(rr),print(RR)
# 
# while len (RR)<N:
#     RR[n-i-1]=rr[i]
# print(rr), print(RR)
# 


#z=[1]+[1]+[1]+[1]+[1]+[1]+[1]+[1]+[1]+[1]+[1]+[1]
# Z=[1]*9  #len(z)
# print(z), print(Z)



 #наоборот реверс
# a=[45,545,7,3694]
# n=len(a)
# b=[0]*n
# 
# for i in range(0, 4):
#     b[i]=a[3-i]
# 
# print(b)

