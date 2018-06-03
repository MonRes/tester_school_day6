import random

def int_input(prompt):
    number = None
    while number is None:
        try:
            number = int(input(prompt))
        except ValueError:
            print('To nie była liczba...')
    return number

lower_bound = int_input('Podaj dolną granicę: ')
upper_bound = int_input('Podaj górną granicę: ')

lower_bound = 0
upper_bound = -1

while lower_bound > upper_bound:
    lower_bound = int_input('Podaj dolną granicę: ')
    upper_bound = int_input('Podaj górną granicę: ')
    if lower_bound > upper_bound:
        print('Początek zakresu nie może być większy niż koniec... Popraw')

target = random.randint(lower_bound, upper_bound) #gdy użytkownik poda mniejszy upper od lowera mozna samego randinta obłożyć try, except

guess = None
count = 0

while target != guess:
    count += 1
    guess = int_input('Podaj liczbę: ')
    if guess < target:
        print ('Za mało!')
    elif guess > target:
        print ('Za dużo!')

print('Gratulacje! Ilość ruchów: ', count)

