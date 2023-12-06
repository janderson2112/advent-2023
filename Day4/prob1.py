from math import pow

sum = 0
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        temp = line.split(':')[1]
        nums = temp.split('|')
        winningNums = nums[0].strip().split()
        myNums = nums[1].strip().split()
        numberOfMatches = 0
        for num in myNums:
            if num in winningNums:
                numberOfMatches += 1
        if numberOfMatches > 0:
            sum += pow(2, numberOfMatches-1)
print(int(sum))