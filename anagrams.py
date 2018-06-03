def are_anagrams(text, text2):
    anagram = {}
    anagram2 = {}

    for char in text.lower():
        anagram[char] = anagram.get(char, 0) + 1
    for char in text2.lower():
        anagram2[char] = anagram2.get(char, 0) + 1

    return anagram == anagram2

print(are_anagrams('cos tamszesc', 'cos tamszesc'))
