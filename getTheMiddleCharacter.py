def get_middle(s):
    string_len = len(s)
    if (string_len % 2):
        return s[int(len(s) / 2)]
    else:
        return ''.join((s[int(len(s) / 2) - 1], s[int(len(s) / 2)]))
    
    
def get_middle_best(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]


print(get_middle("test"))