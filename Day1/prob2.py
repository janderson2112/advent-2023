import re

def replaceNum(num):
    if num.isnumeric():
        return num
    else:
        match num:
            case 'one':
                return '1'
            case 'two':
                return '2'
            case 'three':
                return '3'
            case 'four':
                return '4'
            case 'five':
                return '5'
            case 'six':
                return '6'
            case 'seven':
                return '7'
            case 'eight':
                return '8'
            case 'nine':
                return '9'

sum = 0
with open('input.txt') as input:
    for line in input:
        line = line.rstrip()
        numList = re.findall(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
        sum += int(replaceNum(numList[0]) + replaceNum(numList[-1]))
print(sum)
