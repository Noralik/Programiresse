# EN=open("96.txt", "r")
# print(EN.readline())

EN=open("96.txt", "r")
list=EN.read()
print(list)
EN.close()


DM=open("ded.txt", "w")
DM.write("Dorogoj ded\n")
DM.write("kak ti pozhivaesh\n")
DM.write("kak gnomi\n")
DM.write("s novim godom\n")
DM.write("poka\n")
DM.close()
