
num = int (input ("Enter a Number"))
temp = num
s = 0
while num > 0:
    a = num%10
    f = 1
    for i in range (1, a+1):
        f = f*i
    s = s+f    
    num = num//10
if s == temp:
    print ("strong number")
else:
    print ("not a strong number")
