# Q - 3 Solve a Quadratic Equation

a = int(input("Enter coeffocient of x^2: "))
b = int(input("Enter coeffocient of x:"))
c = int(input("Enter constant term:"))

#condition for a Quadratic Equation
if a == 0:
    print ("this is not a Quadratic Equation as x^2's coefficient cannot be zero")

# calculating discriminant
dis = (b * b) -( 4 * a * c)

# checking condition for discriminant
if dis > 0:
    print("The equation has real and different roots")
    print((-b + (dis**0.5)/(2 * a)))
    print((-b - (dis**0.5)/(2 * a))) 
elif dis == 0: 
    print("The equation has real and same roots") 
    print(-b / (2 * a)) 
      
# when discriminant is less than 0
else:
    print("The equation has Complex Roots") 
