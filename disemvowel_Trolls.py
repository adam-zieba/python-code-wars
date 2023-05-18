def disemvowel(string_):
    vowels = ["a", "e", "i", "u", "o", "A", "E", "I", "U", "O"]
    string_to_list = [i for i in string_ if i not in vowels]
    new_string = "".join(str(x) for x in string_to_list)
    return new_string



def disemvowel_best(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


print(disemvowel("This website is for losers LOL!"))