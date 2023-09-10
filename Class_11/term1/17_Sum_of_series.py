#Q 17 -  print the sum of series:      x+ x2 + x3 + x4 + x5  
#                                         2!   3!   4!   5!

x=int (input ("Enter a number: "))
n=int (input ("Enter a number: "))
s=0
for i in range (1, n+1):
    f=1
    for j in range (1, i+1):
        f = f*j
        s = s+(x**i/f)
print(s)    
