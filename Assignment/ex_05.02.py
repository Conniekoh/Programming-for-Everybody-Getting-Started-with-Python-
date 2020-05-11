
num = 0
tot = 0.0
while True :
    sval = input("Enter a Number: ")
    if sval == 'done' :
        break
    fval = float(sval)
    print(fval)
    num = num + 1
    tot = tot + fval
print ('All Done')
print (tot,num,tot/num)
