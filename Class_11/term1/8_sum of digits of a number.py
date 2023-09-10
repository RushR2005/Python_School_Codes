# Q8 - find the sum of digits of a number

x = int(input("Enter a number:"))
s = 0
while x > 0:
    s = s + (x%10)
    x = x // 10
print (s)
