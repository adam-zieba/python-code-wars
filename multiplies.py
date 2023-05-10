def solution(number):
    sum = 0
    if number > 0:
        for x in range(number):
            if (x % 3 == 0) or (x % 5 == 0):
                sum = x + sum
    else:
      return sum
  
    return sum

def solution_best(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


solution(6)