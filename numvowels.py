def num_vowels(input):
    # vowels = ['a','e','i','o','u']
    vowels = "aeiouAEIOU"
    count = 0

    for character in input:
        if character in vowels:
            count += 1
    print (f'The number of vowels in "{input}" is {count}.')

num_vowels("this is my country")

def num_vowelsV1(input):
    vowels = "aeiouAEIOU"
    count = len([c for c in input if c in vowels]) # list comprehension
    print (f'The number of vowels in "{input}" is {count}.')

num_vowelsV1("this is my country")





