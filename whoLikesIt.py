
# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python
def likes(names):
    like = "like this"
    likes = "likes this"
    if len(names) == 0:
        return f"no one {likes}"
    elif len(names) == 1:
        return f"{names[0]} {likes}"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} {like}"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} {like}"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others {like}"



# https://www.codewars.com/kata/reviews/564425cc55d0e45b8c000087/groups/564ab1bc633fa1f3310000cb
def likes_best(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

print(likes(['Peter']))