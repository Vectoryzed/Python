import re

fhand = open('regex_sum.txt')
numlist = list()

for line in fhand:
    line = line.split(',')
    line = ' '.join(line)
    print("The current line is", line)
    stuff = re.findall('[0-9]+', line)
    if (len(stuff) < 1):
        continue
    for num in stuff:
        print("The current number is", num)
        num = int(num)
        numlist.append(num)

sumlist = sum(numlist)

print("The sum is", sumlist)