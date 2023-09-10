#Q 10 - check whether a given number is a palindrome or not

num = int(input("Enter a number: "))
numval = num
rev=0

while num > 0:
    a = num%10
    rev=(rev*10) +a
    num = num//10
print ("reverse number=", rev)

if rev == numval:
    print(numval, "is a palindrome")
else:
    print (numval, "is not a palindrome")
