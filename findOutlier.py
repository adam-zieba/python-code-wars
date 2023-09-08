# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python

def find_outlier(integers):
    odd_count = 0
    even_count = 0
    
    for i in integers:
        if (i % 2 == 0):
            even_count += 1
        else:
            odd_count += 1
            
    if (even_count == 1):
        for i in integers:
            if (i % 2 == 0):
                return i
    elif (odd_count == 1):
        for i in integers:
            if (i % 2 != 0):
                return i
            

# https://www.codewars.com/kata/reviews/5567bb44bbb6cdc5d2000022/groups/56af9f3b29dda470e3000012

def find_outlier_best(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

find_outlier([2, 4, 6, 8, 10, 3])