def findPower(entry) -> int:
    minDict = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    rounds = entry.split(';')
    for round in rounds:
        colorTotals = round.split(',')
        for colorTotal in colorTotals:
            temp = colorTotal.strip().split(' ')
            color = temp[1]
            num = int(temp[0])
            if num > minDict[color]:
                minDict[color] = num
    return minDict['red'] * minDict['green'] * minDict['blue']

sum = 0
with open('input.txt') as input:
    for line in input:
        temp = line.split(':')
        gameId = temp[0].split(" ")[1]
        sum += findPower(temp[1])
print(sum)