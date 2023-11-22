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






print(move_zeros([1, 0, 1, 2, 0, 1, 3]))