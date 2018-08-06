# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters
# (so you can just rearrange the letters to get a different phrase or word).

def anagram(s1,s2):

    s1 = s1.replace(" ","")
    s2 = s2.replace(" ","")
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False

    letter_count = {}
    for letter in s1:
        if letter_count.get(letter) is None:
            letter_count[letter] = 0
        letter_count[letter] += 1

    for letter in s2:
        if letter_count.get(letter) is None:
            return False
        letter_count[letter] -= 1

    for count in letter_count.values():
        if count != 0 :
            return False

    return True


# print(anagram('dog','god'))
print(anagram('Clint eastwood','old west action'))
# print(anagram('aa','bb'))
