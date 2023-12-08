from collections import defaultdict
from copy import deepcopy
import logging

logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

# Dictionary used for encoding hands as floating point values
PRIORITY_DICT = {
    'A': '14', 
    'K': '13', 
    'Q': '12', 
    'J': '11', 
    'T': '10', 
    '9': '09', 
    '8': '08', 
    '7': '07', 
    '6': '06', 
    '5': '05', 
    '4': '04', 
    '3': '03', 
    '2': '02', 
    '1': '01'
}

# Encodes the hand order as a floating point value for comparison
def encodeOrder(hand):
    encoding = '0.'
    for c in hand:
        encoding = encoding + PRIORITY_DICT[c]
    return float(encoding)

# Determines relative strength of each hand
def determineStrength(hand):
    encoding = encodeOrder(hand)
    cardDict = defaultdict(int)
    for c in hand:
        cardDict[c] += 1
    threeFlag = False
    twoFlag = False
    for key in cardDict.keys():
        if cardDict[key] == 5:
            return 6 + encoding
        elif cardDict[key] == 4:
            return 5 + encoding
        elif cardDict[key] == 3:
            threeFlag = True
        elif cardDict[key] == 2:
            if twoFlag:
                return 2 + encoding
            else:
                twoFlag = True
    if twoFlag and threeFlag:
        return 4 + encoding
    elif threeFlag:
        return 3 + encoding
    elif twoFlag:
        return 1 + encoding
    else:
        return 0 + encoding


# Function passed into sorted function as key
def sortFunction(handObj):
    return handObj['strength']


handList = []
with open('input.txt') as input:
    for line in input:
        elements = line.split()
        obj = {
            'hand': elements[0],
            'strength': determineStrength(elements[0]),
            'bid': elements[1]
        }
        handList.append(deepcopy(obj))
handListSorted = sorted(handList, key=sortFunction)
for i in handListSorted:
    logging.info(f'{i['hand']} - {i['strength']}')
totalWinnings = 0
for i in range(0, len(handListSorted)):
    bid = int(handListSorted[i]['bid'])
    rank = i+1
    totalWinnings += bid*rank
    logging.info(f'Hand: {handListSorted[i]["hand"]} - Rank: {rank} - Bid: {bid} Earnings: {rank*bid}')
logging.info(f'Total Winnings: {totalWinnings}')