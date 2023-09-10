#Q6 - check if the input year is a leap year or not

year = int(input("Enter the year:"))
if ((year % 4 == 0 and year % 100 != 0)or year % 400 == 0):
     print (year,"was a leap year")
else:
    print (year , "was not a leap year")
