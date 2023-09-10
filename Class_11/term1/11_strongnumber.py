# Q 11 - check if a number is a strong number

num = int(input("Enter a number:"))  
numval = num  

while(num):  
    i = 1
    fact = 1
    rem = num%10  
    while(i<=rem):  
        fact=fact*i   # Find factorial of each number  
        i=i+1  
    s = s + fact  
    num = num//10  
if s == numval:  
    print(numval, " is a strong number")  
else:  
    print(numval, " is not a strong number")
