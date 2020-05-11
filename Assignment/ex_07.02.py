#assignment 07.02.py
# Use words.txt as the file name
count = 0
average = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    pos = line.find[" "]
    number = line[pos:].rstrip()
    number = float(number)
    count = count + 1
    average = average + number
print("Average spam confidence:", average/count)
