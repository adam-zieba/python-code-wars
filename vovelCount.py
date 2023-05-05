def get_count(sentence):
    vovels = ['a', 'e', 'i', 'o', 'u']
    total_vovel_number = 0

    for letters in vovels:
        total_vovel_number += sentence.count(letters)

    print(total_vovel_number)
    return total_vovel_number

def get_count_best(sentence):
    return sum(1 for let in sentence if let in "aeiouAEIOU")






get_count("abracadabra")