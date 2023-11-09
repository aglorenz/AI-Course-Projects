from collections import Counter

def first_unique_char(sentence):
    counts = Counter(sentence)
    for char in sentence:
        if counts[char] == 1:
            return char
        else:
            return None

print (first_unique_char("now is the time"))