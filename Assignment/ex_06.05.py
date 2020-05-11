text = "X-DSPAM-Confidence:    0.8475"
first = text.find('0')
print(first)
second = text.find('5')
print(second)
last = text[first:]
number = float(last)
print(number)
