# Q15 - factorial of a given no

num = int(input("Enter a number:"))
fact =  1

while num != 0:
    fact = fact * num
    num -= 1

print ("Factorial of number is", fact)
