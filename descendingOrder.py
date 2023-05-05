def descending_order(num):
    splitted_digits = []
    
    for x in str(num):
        splitted_digits.append(int(x))
    
    print(f"Sorted digits: {sorted(splitted_digits, reverse=True)}")
    
    num_of_loops = 0
    
    #while splitted_digits[8] != min_value:
    while num_of_loops < len(splitted_digits) - 1:
        
        
        max_value = max(splitted_digits[num_of_loops], splitted_digits[(len(splitted_digits)) - 1 ])
        print(f"Index of the element: {splitted_digits.index(max_value)}")
        
        index_of_max_value = splitted_digits.index(max_value)
        temporary_number = splitted_digits[num_of_loops]
        
        
        '''
        numA = splitted_digits[num_of_loops]
        splitted_digits[num_of_loops] = max_value
        numB = splitted_digits[num_of_loops + 1]
       
                
        if numA < numB:
            splitted_digits[num_of_loops] = numB
            splitted_digits[num_of_loops + 1] = numA
                '''
        print(splitted_digits)
        num_of_loops += 1
        
    s = [str(integer) for integer in splitted_digits]
    a_string = "".join(s)
    
    res = int(a_string)
    print(res)
    #return splitted_digits[4]
    
descending_order(123456789)