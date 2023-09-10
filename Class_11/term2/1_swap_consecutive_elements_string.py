str1 = input("Please Enter String : ")
p = ""

for i in range(0,len(str1),2):
    p = p + str1[i+1] + str1[i]
print(p)


