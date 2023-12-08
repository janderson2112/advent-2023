lines = []
with open('input.txt') as input:
    for line in input:
        lines.append(line.strip())
timeLine = lines[0]
distLine = lines[1]
time = lines[0].split(':')[1].strip().split()
distance = lines[1].split(':')[1].strip().split()
totalTime = ''
for t in time:
    totalTime = totalTime + t
totalDistance = ''
for d in distance:
    totalDistance = totalDistance + d
totalTime = int(totalTime)
totalDistance = int(totalDistance)
# i = how long to hold for
for i in range(0, totalTime+1):
    iDist = totalTime - i
    iDist = iDist * i
    if iDist > totalDistance:
        startIndex = i
        endIndex = totalTime - i
        waysToWin = endIndex - startIndex + 1
        print(waysToWin)
        break