sum = 0
with open('input.txt') as input:
    for line in input:
        line = line.rstrip()
        intList = [char for char in line if char.isnumeric()]
        sum += int(intList[0] + intList[-1])
print(sum)