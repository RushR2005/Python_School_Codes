# Q-9 - count the number of digits in a number  

number = int(input("Enter the number:"))
counter = 0

while number != 0:
    number //= 10
    counter += 1

print("Number of digits are ", counter)
