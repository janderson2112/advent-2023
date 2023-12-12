class Node:
    def __init__(self, right, left, value):
        self.right = right
        self.left = left
        self.value = value

    def traverseLeft(self):
        return self.left
    
    def traverseRight(self):
        return self.right
    
    def getValue(self):
        return self.value
    
class Edge:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

    def getSource(self):
        return self.source
    
    def getDest(self):
        return self.dest
    
nodeDict = {}
with open('input.txt') as input:
    pattern = ''
    for line in input:
        if pattern == '':
            pattern = line.strip()
        else:
            vals = line.split('=')
            source = vals[0].strip()
            dests = vals[1]
            dests = dests.split(',')
            dests = [val.replace('(','').replace(')','').strip() for val in dests]
            nodeDict[source] = {
                'L': dests[0],
                'R': dests[1]
            }
currentNode = 'AAA'
direction = 0
steps = 0
while currentNode != 'ZZZ':
    currentNode = nodeDict[currentNode][pattern[direction]]
    steps += 1
    if direction+1 < len(pattern):
        direction += 1
    else:
        direction = 0
print(f"Number of Steps: {steps}")