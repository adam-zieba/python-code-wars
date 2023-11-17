# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python

def duplicate_count(text):
    testToLower = text.lower()
    occured = 0
    listOfOccured = []
    for i in testToLower:
        if testToLower.count(i) >= 2 and i.lower() not in listOfOccured:
            listOfOccured.append(i.lower())
            occured += 1

    return int(occured)

# https://www.codewars.com/kata/reviews/54bf22f66150e17854000193/groups/54bf92f26cac4181ef00071f

def duplicate_count_best(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])


duplicate_count("Indivisibilities")