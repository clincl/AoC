'''
Input:
https://adventofcode.com/2018/day/1/input
'''
'''
Part 1
Sum Input File
'''
def frequencies(input = 'input.txt'):
    changes = [int(line) for line in open(input)]
    return changes
#print(sum(frequencies()))
'''
Part 2
Find the first frequency to appear twice.
'''
from itertools import accumulate
def calibration(frequencies, loop = 1):
    seen = set([0])
    looper = list(accumulate(loop*frequencies))
    print(len(looper))
    for int in looper:
        if int in seen:
            print('seen: ' + str(int))
            return int
        else:
            seen.add(int)
    print(loop)
    seen = set([0])
    calibration(frequencies, loop + 1)
calibration(frequencies())
#for int in accumulate(2*frequencies()):print(int)
#print(accumulate(2*frequencies()))
