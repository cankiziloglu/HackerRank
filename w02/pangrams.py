# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram
# in the English alphabet. Ignore case. Return either 'pangram' or 'not pangram' as appropriate.

import string


def pangrams(s):
    letters = set(string.ascii_lowercase)
    sentence = set(s.lower())

    if letters - sentence:
        return "not pangram"
    else:
        return "pangram"


s = input("sentence")
print(pangrams(s))
