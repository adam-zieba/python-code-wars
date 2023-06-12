def spin_words(sentence):
    split_sentence = sentence.split(" ")
    new_string = ""
    print(split_sentence)
    for w in split_sentence:
        if len(w) >= 5:
            reversed_word = w [::-1]
            new_string = (new_string + " " + reversed_word).lstrip()
        else:
            new_string = (new_string + " " + w).lstrip()
            
    return new_string


def spin_words_best(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

print(spin_words("only that one or or string a Spaces consist with string a words or and will like of with than"))