def num_vowels(input):
    vowels = ['a','e','i','o','u']
    count = 0

    for i in range(len(input)):
        if input[i] in vowels:
            count += 1
    print (f'The number of vowels in "{input}" is {count}.')

num_vowels("this is my country")


