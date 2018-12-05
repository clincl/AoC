'''
type: letter
polarity: lowercase or uppercase
same type + different polarity = cancel
Part 1
Final Result?
'''
from itertools import tee
def reaction(input='input.txt'):
    with open(input) as file:
        input = list(file.read().replace('\n',''))
        prevInput = 0
        while True:
            compare = input.copy()
            del compare[0]

            delete = []
            store = []

            for indice, char in enumerate(compare):
                try:
                    if  indice == store[0] + 2 and char == store[1]:
                        #print(char, compare[indice-2])
                        store = []
                        print(prevInput, len(input))

                        continue
                except IndexError:
                    pass
                if char.upper() == input[indice].upper():
                        #print(char, compare[indice])
                    delete.append(indice)
                    delete.append(indice+1) # cancels need to be removed
                    store = [indice, char]

                #print(len(input), len(compare), indice, counter)

            delete.reverse() #reverse because list gets shortened
            #print(len(delete))
            print(prevInput, len(input))
            if prevInput == len(input):
                break
            for i in delete:
                del input[i]
            prevInput = len(input.copy())
            print(prevInput, len(input))
        print(len(input))
reaction()
