def isPossible(ruleDict, entry) -> bool:
    rounds = entry.split(';')
    for round in rounds:
        colorTotals = round.split(',')
        for colorTotal in colorTotals:
            temp = colorTotal.strip().split(' ')
            color = temp[1]
            num = temp[0]
            if int(num) <= ruleDict[color]:
                continue
            else:
                print(f'Num: {num} is greater than limit for {color}: {ruleDict[color]}')
                return False
    return True

ruleDict = {
    'red': 12,
    'green': 13,
    'blue': 14
}
sum = 0
with open('input.txt') as input:
    for line in input:
        temp = line.split(':')
        gameId = temp[0].split(" ")[1]
        if isPossible(ruleDict, temp[1]):
            sum += int(gameId)
print(sum)