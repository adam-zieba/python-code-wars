# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python

def accum(s):
    iterable = 1
    finalString = ''
    for i in s:
      finalString += (i * iterable + "-").capitalize()
      iterable += 1
    return finalString.rstrip('-')


# The best solution
# https://www.codewars.com/kata/reviews/5667e9e7ffbf34676800005f/groups/566895d720927c3809000031
def accum_best(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

accum("abcd")