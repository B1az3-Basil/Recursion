import sys
import random
sys.setrecursionlimit(2000)

def find_min(element):
    """TODO: complete for Step 1"""
    ''' Finds the minimum number in the list it is given'''
    i = 0
    print("hello")

    if len(element) == 0:
        return -1

    while i < len(element):
        check = str(element[i])

        if check.isalpha() == True :
            return -1
        if type(element[i]) == float:
            pass
        else:
            element[i] = int(element[i])
        i += 1

    if len(element) > 1:
        i = 0

        while i < len(element):

            if i == len(element) - 1:
                i = 0

                if element[i] > element[i + 1]:
                    element.pop(i)
                    return find_min(element)

                else:
                    element.pop(i + 1)
                    return find_min(element)

            elif element[i] > element[i + 1]:
                element.pop(i)
                return find_min(element)

            i += 1

    else:
        return element[0]

def sum_all(element):
    """TODO: complete for Step 2"""
    ''' Adds all the numbers which were given in the list'''
    i = 0
    if len(element) == 0:
        return -1

    while i < len(element):
        check = str(element[i])

        if check.isalpha() == True:
            return -1
        
        if type(element[i]) == float:
            pass
        else:
            element[i] = int(element[i])

        i += 1

    if len(element) > 1:
           ans = element[0] + element[1]
           element[1] = ans
           element.pop(0)
           return sum_all(element)

    else:
        return element[0]


def find_possible_strings(character_set, n):
    k = len(character_set) ** n
    for i in range(len(character_set)):
        if str(character_set[i]).isnumeric():
            return []
    return make_the_strings(0,character_set, [], n, k)


def make_the_strings(index,alpha,sets, n, k):
    
    if k == 0:
        sets.sort()
        return sets

    while True:
        i = 0
        str_l = []
        while i < n:
            c = alpha[random.randint(0, len(alpha) - 1)]
            str_l.append(c)
            i += 1
        str = ''.join(str_l)
    
        if str not in sets:
            sets.insert(index,str)
            index += 1
            
            return make_the_strings(index,alpha, sets , n, k - 1)

