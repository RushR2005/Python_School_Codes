# Q - 7 find the largest number among the three input numbers without logical operator/nested if

fn = float(input("Enter first number:"))
sn = float(input("Enter second number:"))
tn = float(input("Enter third number:"))

if fn == sn == tn:
    print ("All of the entered nubers are equal, no one is the greatest")

#checking for 1
elif fn > sn:
    if fn > tn:
        print (fn, "is the greatest number out of all entered numbers")
    elif fn == tn:
        print (fn, "&", tn, "both are the greatest")
    else:
        print (tn, "is the greatest")
elif fn > tn:
    if fn > sn:
        print (fn, "is the greatest number out of all entered numbers")
    elif fn == sn:
        print (fn, "&", sn, "both are the greatest")
    else:
        print (sn, "is the greatest")

#checking for 2
elif sn > fn:
    if sn > tn:
        print (sn, "is the greatest number out of all entered numbers")
    elif sn == tn:
        print (sn, "&", tn, "both are the greatest")
    else:
        print (tn, "is the greatest")
elif sn > tn:
    if sn > fn:
        print (sn, "is the greatest number out of all entered numbers")
    elif fn == sn:
        print (fn, "&", sn, "both are the greatest")
    else:
        print (fn, "is the greatest")

#checking for 3
elif tn > fn:
    if tn > sn:
        print (tn, "is the greatest number out of all entered numbers")
    elif sn == tn:
        print (sn, "&", tn, "both are the greatest")
    else:
        print (sn, "is the greatest")
elif tn > sn:
    if tn > fn:
        print (sn, "is the greatest number out of all entered numbers")
    elif fn == tn:
        print (tn, "&", sn, "both are the greatest")
    else:
        print (fn, "is the greatest")
