def is_pangram(string):
    count = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char in string:
            count += 1
    if count == 26:
        return True
    else:
        return False
    
print(is_pangram("The quick brown fo jumps over the lazy dog"))