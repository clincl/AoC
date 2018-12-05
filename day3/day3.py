'''
1000 inches on each side. (1000x1000)

A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall.

Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:
...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
'''

'''
Part 1
How many square inches of fabric are within two or more claims?
Solution:
Create 1000 arrays with 1000 indices
Loop through each entry of the input.txt to record the positions.
For each use, add 1 to the array indice.
e.g. 5,5 5,5 the spaces filled would be 6=left+1 to 11=left +5, 6=top+1 to 11=top+5
in the actual array: the first would be array[6][6] to array[11][11]
@ space1 number comma number colon space2 number x number
'''
def whatever():
    checker = 1
    at = 0
    comma = 0
    colon = 0
    x = 0
    for array, line in enumerate(open('input.txt')):
        values = {'left':line[at+2:comma], 'top':line[comma+1:colon], 'x':line[colon+2:x], 'y':line[x+1:-1]}
        if array == 1346:
            #for counter, char in enumerate(line):
            #    print(str(counter) + ': ' + char)
            #print('char at 15 is ' + line[15])
            for indice, char in enumerate(line):
                if char == ':': print(': is at ' + str(indice))
            #print(values)
            #print(line[comma], line[colon], line[x])
            #print(comma, colon, x)
        for indice, char in enumerate(line):
            if array == checker:
                print(values, line[comma], line[colon], line[x])
                #print(array, comma, colon, x)
                checker += 1 #so array can check checker again
            if char == '@': at = indice
            if char == ',': comma = indice
            if char == ':': colon = indice
            if char == 'x': x = indice

whatever()
