# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python

def duplicate_encode(word):
    lower = word.lower()
    new_list = []
    for i in lower:
        if (lower.count(i) > 1):
            new_list.append(")")
        else:
            new_list.append("(")

    return ''.join(new_list)

# https://www.codewars.com/kata/reviews/55249a95de8b4b5ae2000464/groups/552540ce2142d7ba24000e65

def duplicate_encode_best(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

print(duplicate_encode("Success"))