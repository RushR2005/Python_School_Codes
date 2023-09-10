# Q 12 - find the LCM of two numbers

n1 = int (input ("Enter 1st Number: "))
n2 = int (input ("Enter 2nd Number: "))

if n1>n2:
    large=n1
    small =n2
else:
    large = n2
    small = n1
answ = large

while answ%small != 0:
    answ = answ+large

print ("LCM is ", answ)
