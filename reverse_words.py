def reverse_words(sentence):
    words_list = sentence.split(' ') # list comprehension
    return ' '.join(reversed(words_list))

print(reverse_words("This is my day today"))