text = 'Quick brown fox'

print(text[0:5:2]) #zacznij od 0 do 5, jeśli chcesz do końca np to zakres [6::2] zacznij na 6 do końca co dwa

print(text[6::-1])

print(text[::-1]) #cały string od końca

numbers = '123, 456, 789'

def split(text, sep):
    parts = []
    start = 0

    for current, char in enumerate(text): #current = index, char = odpowiadajacy znak currentowi w tekscie
        if char == sep:
            parts.append(text[start:current]) #dodaj text od np 0 do 3 indeksu
            start = current + 1 #zwiększ current o 1
    parts.append(text[start:]) #po wykonanej pętli for dodajemy jeszcze jeden brakujący element
    return parts

print(split(numbers, ','))