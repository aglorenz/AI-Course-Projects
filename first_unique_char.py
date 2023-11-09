from collections import Counter

def first_unique_char(sentence):
    counts = Counter(sentence)
    for char in sentence:
        if counts[char] == 1:
            print(f'The first unique character in "{sentence}" is {char}')
            break

first_unique_char("now is the time")