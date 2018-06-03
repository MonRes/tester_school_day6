example = {'a': 1, 'b': 2, 'c': 3}

print(example['a']) # dla 'd' dostaniemy keyerror d

print(example.get('d', 5)) #sprawdza czy znajduje się d, jeśli nie to dodaje ją do słownika z wartością 5
