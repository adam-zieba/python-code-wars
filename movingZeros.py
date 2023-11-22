# https://www.codewars.com/kata/52597aa56021e91c93000cb0/python

def move_zeros(lst):
    newList = []
    howManyZeroes = lst.count(0)
    for x in lst:
        if x != 0:
            newList.append(x)
    
    while howManyZeroes > 0:
        newList.append(0)
        howManyZeroes = howManyZeroes - 1

    return newList


# https://www.codewars.com/kata/reviews/57cb52c733c32f4c48000076/groups/57cb983f58da9ee25b000126
def move_zeros_best(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))




print(move_zeros([1, 0, 1, 2, 0, 1, 3]))