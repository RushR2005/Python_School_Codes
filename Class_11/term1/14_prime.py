#Q-14 - check if a number is a prime number

num = int(input("Enter a number:"))

for i in range(2,num):
    if num%i == 0:
        print (num, """ is not a Prime number,
               it is a Composite number""")
        break
else:
    print (num, " is a Prime number")
