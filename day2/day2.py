'''
Count ID's with exactly 2 or 3 of the same letter.
If a ID has multiple 2's or 3's, it only counts for one.
Multiply number of 2's and 3's to get checksum.

Example:
abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?
'''
def check2(id):
    for char in set(id):
         return 1 if id.count(char) == 2 else 0

def check3(id):
    for char in set(id):
         return 1 if id.count(char) == 3 else 0

def checksum(input = 'input.txt'):
    char2 = 0
    char3 = 0
    file = [line for line in open(input)]
    for count, id in enumerate(file):
        if count == 1:
            print(len(set(id)))
        char2 += check2(id)
        char3 += check3(id)
    print('p count: ' + str(file[0].count('p')))
    print('check2 result: ' + str(check2(file[0])))
    print(len(file[0]), len(set(file[0])), check2(file[0]), check3(file[0]))
    return [char2, char3, char2 * char3]
print(checksum())
