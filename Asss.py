import re

fname = open("asss.txt")

sum = 0
count = 0
for line in fname:
    f = re.findall('[0-9]+',line)
    for num in f:
        count+= 1
        sum = sum + (int(num))
print("there are ",count,"value with a sum of ",sum)