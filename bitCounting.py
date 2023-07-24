def count_bits(n):
    if n >=0:
      bin_number = bin(n)
      count_bin = bin_number.count("1", 2)
      return count_bin
    else:
        print("The provided value should be not less than 0")


print(count_bits(10))