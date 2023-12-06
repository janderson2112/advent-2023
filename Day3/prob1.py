def isSymbol(char) -> bool:
    if char.isnumeric():
        return False
    if char == '.':
        return False
    else:
        return True

charMatrix = []
symbolCoords = []
lineLength = 0
totalLine = ''
totalLength = 0
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        totalLength += len(line)
        totalLine = totalLine + line
        if lineLength == 0:
            lineLength = len(line)
        elif lineLength != len(line):
            print('WARNING: Not all lines are of equal lenght. Algorithm will provide a faulty answer.')
print(totalLine)
print(lineLength)
print(totalLength)

currentNum = ''
symbol = False
sum = 0
for i in range(0, totalLength):
    char = totalLine[i]
    if char.isnumeric():
        currentNum = currentNum + char
        if i%lineLength != 0:
            if isSymbol(totalLine[i-1]):
                symbol = True
            if i > lineLength:
                if isSymbol(totalLine[i-(lineLength+1)]):
                    symbol = True
            if i+lineLength-1 < totalLength:
                if isSymbol(totalLine[i+(lineLength-1)]):
                    symbol = True
        if (i+1)%lineLength != 0:
            if isSymbol(totalLine[i+1]):
                symbol = True
            if i > lineLength:
                if isSymbol(totalLine[i-(lineLength-1)]):
                    symbol = True
            if i+lineLength+1 < totalLength:
                if isSymbol(totalLine[i+(lineLength+1)]):
                    symbol = True
        if i-lineLength > 0:
            if isSymbol(totalLine[i-lineLength]):
                symbol = True
        if i+lineLength <= totalLength:
            if isSymbol(totalLine[i+lineLength]):
                symbol = True
    else:
        if symbol == True:
            sum += int(currentNum)
            print(currentNum)
        currentNum = ''
        symbol = False
print(f'SUM: {sum}')







# for i in range(0, len(charMatrix)):
#     for j in range(0, len(charMatrix[i])):
#         isGood = False
#         if charMatrix[i][j].isnumeric():
#             if j != 0:
#                 if not charMatrix[i][j-1].isnumeric() and not charMatrix[i][j-1] == '.':
#                     isGood = True