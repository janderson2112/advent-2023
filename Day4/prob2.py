inputLength = 0
with open('input.txt') as input:
    for line in input:
        inputLength += 1

scoreList = [0]
for i in range (1, inputLength+1):
    scoreList.append(0)
print(scoreList)

currentLine = 0
with open('input.txt') as input:
    for line in input:
        currentLine += 1
        scoreList[currentLine] += 1
        line = line.strip()
        temp = line.split(':')[1]
        nums = temp.split('|')
        winningNums = nums[0].strip().split()
        myNums = nums[1].strip().split()
        for i in range(1, scoreList[currentLine]+1):
            numberOfMatches = 0
            for num in myNums:
                if num in winningNums:
                    numberOfMatches += 1
            for i in range(1, numberOfMatches+1):
                scoreList[currentLine+i] += 1

total = 0
for i in range(1, len(scoreList)):
    total += scoreList[i]
print(scoreList)
print(total)