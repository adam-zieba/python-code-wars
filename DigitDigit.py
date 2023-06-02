def square_digits(sum):
    sum_string = str(sum)
    concat_string = ""
    for i in sum_string:
        multiply = int(i) * int(i)
        concat_string += str(multiply)
    
    return int(concat_string)
    
    
    
def square_digits_best(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
    
    
square_digits(0)