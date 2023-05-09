def make_negative(number):
    if number > 0:
      negative_number = str(number)
      negative_number = "-" + negative_number
      return int(negative_number)
    else:
        return number


def make_negative_best(number):
    return -abs(number)


print(make_negative(42))