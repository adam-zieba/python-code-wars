def find_multipies(integer, limit):
    equal_counter = []
    basic_number = integer
    sum = 0
    if (limit % integer) == 0:
        while sum < limit:
            sum = basic_number + sum
            equal_counter.append(sum)
    else:
        while sum <= limit - integer:
            sum = basic_number + sum
            equal_counter.append(sum)

    return equal_counter


def find_multiplies_best(integer, limit):
    return list(range(integer, limit+1, integer))


find_multipies(2,11)