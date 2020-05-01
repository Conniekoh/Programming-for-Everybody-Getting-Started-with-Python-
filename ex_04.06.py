def computepay(fh, fr) :

	if fh > 40 :
    	reg = fh * fr
    	opt = (fh - 40.0) * (fr * 0.5)
    	xp = reg + opt
	else :
   	 	xp = fh * fr
	return xp

sh = input("Enter Hours: ")
sr = input("Enter Rates: ")
fh = float(sh)
fr = float(sr)

x = computepay(fh, fr)
print("Pay", x)
