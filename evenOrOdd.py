def even_or_odd(number):
    
    if (number % 2) == 0:
        return "Even"
    else:
        return "Odd"
    
    
# https://www.codewars.com/kata/reviews/53da3de52a289a37bc00128a/groups/53da5bcf4a51681af4001010
def even_or_odd_best(number):
    return 'Odd' if number % 2 else 'Even'




even_or_odd(-123)
even_or_odd_best(-123)