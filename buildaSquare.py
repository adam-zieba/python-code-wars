def generate_shape(n):
    string = ""
    if n > 1:
      for x in range(n -1):
          x = "+"
          string += str((x * n) + "\n")
    else:
        x = "+"
        return x * n
        
        
    string += str((x * n))
    return string



def generate_shape_best(integer):
    return '\n'.join('+' * integer for i in range(integer))

generate_shape(1)