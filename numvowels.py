def num_vowels(input):
    vowels = ['a','e','i','o','u']
    count = 0

    for character in input:
        if character in vowels:
            count += 1
    print (f'The number of vowels in "{input}" is {count}.')

num_vowels("this is my country")


