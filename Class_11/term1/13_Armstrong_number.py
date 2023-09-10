#Q 13 - Check Armstrong number (for 3 digits)

num = int(input("Enter a Number: "))
numval = num
s = 0

while num > 0:
    b = num%10
    s = s+(b*b*b)
    num = num//10
if s == numval:
    print(numval, "is an Armstrong number")
else:
    print(numval, "is not an Armstrong number")
