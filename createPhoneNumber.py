# https://www.codewars.com/kata/525f50e3b73515a6db000b83/python

def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"



# https://www.codewars.com/kata/reviews/59b1a938182024506b00081d/groups/59b1ac8f182024a5be000848
def create_phone_number_best(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)



create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])