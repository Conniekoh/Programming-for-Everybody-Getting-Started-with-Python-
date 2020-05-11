#
largest = "10"
smallest = "2"
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        fnum = float(num)
    except:
        print("Invalid input")


print("Maximum is", largest)
print("Minimum is", smallest)
