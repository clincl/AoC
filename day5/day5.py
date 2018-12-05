'''
type: letter
polarity: lowercase or uppercase
same type + different polarity = cancel
Part 1
Final Result?
'''
from string import ascii_lowercase as lower, ascii_uppercase as upper
def stringy(input = 'input.txt'):
    with open(input) as file:
        input = file.read().strip()
        return input

def reaction(input):
    length = len(input)
    subs = set([])
    for counter, char in enumerate(lower):
        subs.add(char + upper[counter])
        subs.add(upper[counter] + char)
    while True:
        for d, combos in enumerate(subs):
            if combos in input:
                input = input.replace(combos, '')
        if length == len(input):
            return length
        length = len(input)

print(reaction(stringy()))
'''

Your puzzle answer was 10368.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
'''
def fix(input = stringy()):
    record = len(input)
    print('xd' + str(record))
    for char in lower: #removing each letter
        input = stringy()
        input = input.replace(char,'')
        input = input.replace(char.upper(),'')
        input = reaction(input) #reacting
        if input < record: #recording lowest
            record = input
    return record
print(fix())
