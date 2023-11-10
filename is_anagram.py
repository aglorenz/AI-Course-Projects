def is_anagram(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

print (is_anagram("how are you","You are how"))