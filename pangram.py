import string

print(string.ascii_lowercase)

def is_pangram(text):
    """ Checks if text is a pangram.

    Args:
        text: string to be checked
    Return:
        True if text is a pangram, False otherwise
    """
    for letter in string.ascii_lowercase:
        if letter not in text:
            return False
        return True

print(is_pangram(text='The quick brown fox jumps over a lazy dog'))


# to rozwiązanie pochłania za dużo mocy obliczeniowej
# bardziej optymalna metoda

def is_pangram2(text):
    found_letters = {}
    for char in text.lower():
        if char.isalpha(): #czy jeden znak jest alfabetyczny, rozpoznaje znaki
            found_letters[char] = 0 #jeśli tak dodajemy wpis, który okupuje miejsce
    if len(found_letters) == len(string.ascii_lowercase):
        return True
    return False

pang = 'The quick brown fox jumps over a lazy dog'

print(is_pangram(pang))

#funkcja działa tak, że zlicza tylko ilość znaków a nie porównuje ich, ale jest optymalna