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
    file = [line.strip() for line in open(input)]
    for count, id in enumerate(file):
        char2 += check(id, 2)
        char3 += check(id, 3)
    return str(char2) + '(pairs) times ' + str(char3) + '(triples) is ' + str(char2 * char3)
#print(checksum())

'''
Part 2
Correct box IDs differ by one character.
What letters are common between the two correct box IDs?
'''
def correctBoxes(input = 'input.txt'):
    file = [line.strip() for line in open(input)]
    file.sort()
    print(file)
    for row, line in enumerate(file):
        mismatches = 0
        for indice, char in enumerate(line):
            if char != file[indice]:
                mismatches += 1
                if mismatches == 2:
                    break
        if mismatches == 1:
            return line, file[row + 1]
''
    #file.reverse().sort()


    '''
    file = [line.strip() for line in open(input)]
    difference = 0 #the index
    for line in file: #loop1 list
        base = list(line) #adds chars to a list
        for line2 in file: #loop2 list
            compare = list(line2) #creates list for comparison
            for charIndex in range(len(line)): #loop characters
                record = 0 #resets each loop
                if compare[charIndex] == base[charIndex]:
                    record += 1
                    difference = charIndex
                    if record == len(line) - 1 and charIndex == len(line):#26
                        print(record)
                        return line[:difference]+line[difference + 1:]
                        #return [line, line2]
                        print(record)#26
                        '''

print(correctBoxes())
