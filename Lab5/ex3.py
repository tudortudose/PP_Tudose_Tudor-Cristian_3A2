def get_vowels_from_string(string):
    vowels = "aeiou"
    found_vowels = []
    for ch in string:
        if ch in vowels:
            found_vowels += [ch]
    return found_vowels


def get_vowels_comprehensive(string):
    return [vowel for vowel in string if vowel in "aeiou"]


print(get_vowels_from_string("Programming in Python is fun"))
print(get_vowels_comprehensive("Programming in Python is fun"))
print(list(filter(lambda x: x in "aeiou", "Programming in Python is fun")))