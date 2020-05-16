name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
counts = dict()
handle = open(name)
for line in handle:
	line = line.strip()
	if line.startswith("From ") :
		person = line.split()
		email = person[1]
        counts[email] = counts.get(email, 0) + 1
	else:
		continue

bigword = None
bigcount = None
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count
print(bigword, bigcount)
