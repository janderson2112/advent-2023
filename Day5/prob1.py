from copy import deepcopy

currentMap = ''
mappingsDict = {
    'seed-to-soil map': [],
    'soil-to-fertilizer map': [],
    'fertilizer-to-water map': [],
    'water-to-light map': [],
    'light-to-temperature map': [],
    'temperature-to-humidity map': [],
    'humidity-to-location map': []
}
with open('input.txt') as input:
    for line in input:
        if 'seeds:' in line:
            seeds = line.strip().split(':')[1].strip()
            seeds = seeds.split()
            seeds = [int(seed) for seed in seeds]
            print(seeds)
        if 'map:' in line:
            currentMap = line.strip().split(':')[0]
        else:
            specs = line.split()
            if len(specs) == 3:
                specObj = {
                    'src': int(specs[1]),
                    'dest': int(specs[0]),
                    'inc': int(specs[2])
                }
                mappingsDict[currentMap].append(deepcopy(specObj))

print(mappingsDict)
locationList = []
for seed in seeds:
    currentVal = seed
    for mapping in mappingsDict.keys():
        currentMapping = mappingsDict[mapping]
        prev = currentVal
        valueSet = False
        for i in currentMapping:
            if i['src'] <= currentVal < (i['src'] + i['inc']):
                # print(f'{i['src']} <= {currentVal} < {(i['src'] + i['inc'])}')
                diff = currentVal - i['src']
                currentVal = i['dest'] + diff
                break
        print(f'Seed: {seed} Mapping {mapping} - {prev} to {currentVal}')
    print(currentVal)
    locationList.append(currentVal)

print(f'Min Location: {min(locationList)}')