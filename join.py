print(','.join(['a', 'b', 'c']))

numbers = '123, 456, 789'

def split(text, sep):
    parts = []
    current_part = []
    for char in text:
        if char != sep:
            current_part.append(char)
        else:
            parts.append(''.join(current_part))
            current_part = []

    parts.append(''.join(current_part))
    return parts

print(split(numbers, ','))