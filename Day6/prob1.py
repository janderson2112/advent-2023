lines = []
with open('input.txt') as input:
    for line in input:
        lines.append(line.strip())
timeLine = lines[0]
distLine = lines[1]
time = lines[0].split(':')[1].strip().split()
distance = lines[1].split(':')[1].strip().split()
time = [int(i) for i in time]
distance = [int(i) for i in distance]
answer = 1
for j in range(0, len(time)):
    t = time[j]
    dist = []
    for i in range(0, t+1):
        tempT = t
        tempI = i
        iDist = 0
        while tempT != 0:
            if tempI != 0:
                tempI -= 1
                tempT -= 1
            else:
                iDist += i
                tempT -= 1
        dist.append(iDist)
    print(dist)
    waysToWin = 0
    for d in dist:
        if d > distance[j]:
            waysToWin += 1
    answer = answer * waysToWin
print(answer)