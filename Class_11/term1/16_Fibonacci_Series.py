# Q-16 - print the Fibonacci Series 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 …

n1 = 0
n2 = 1
count = 0

print("Fibonacci sequence:")
while count < count+1:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
