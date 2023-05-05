def descending_order(num):
    splitted_digits = []
    
    for x in str(num):
        splitted_digits.append(int(x))
        
    splitted_digits_sorted = sorted(splitted_digits, reverse=True)
    s = [str(integer) for integer in splitted_digits_sorted]
    a_string = "".join(s)
    res = int(a_string)
    print(res)
    return res
    
descending_order(123456789)