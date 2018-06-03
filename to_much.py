import random

print(random.random()) # liczba z przedziału od [0, 1)
print(random.randint(0, 10)) # liczba od 0 do 10 całkowite z obu stron przedział zamknięty

print(random.choice(['a', 'b', 'c'])) # wybierze element z listy



data = float(input('Podaj liczbę z przedziału od 0 do 10 '))
rnd = random.randint(0, 10)




while data != rnd:
    if data < rnd:
        print('za mało')
        data = float(input('Sróbuj jeszcze raz '))
    elif data > rnd:
        print ('za dużo')
        data = float(input('Spróbuj jeszcze raz '))
    else:
        print('Error')

print('udało ci się, podana liczba to', rnd)