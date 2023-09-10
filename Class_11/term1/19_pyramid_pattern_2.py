# Q 19 - printing pyramid patterns 2

sp=' '
num = 4
for i in range (1,6):
    print (sp*num, end='')
    for j in range (1, i+1):
        print ("* ", end='')
    print ()
    num = num-1



