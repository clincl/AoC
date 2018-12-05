'''
Part 1
checksum = pairs * triples
each string counts a max of 1 pair and 1 triple
What is the checksum for your list of box IDs?
'''
#Using Counter from collections module is another way to solve
def check(id, count):
    for char in set(id):
        if id.count(char) == count: return 1
    return 0

def checksum(input = 'input.txt'):
    char2 = 0
    char3 = 0
    file = [line for line in open(input)]
    for count, id in enumerate(file):
        char2 += check(id, 2)
        char3 += check(id, 3)
    return str(char2) + '(pairs) times ' + str(char3) + '(triples) is ' + str(char2 * char3)
print(checksum())

'''
Part 2
Correct box IDs differ by one character.
What letters are common between the two correct box IDs?
'''
