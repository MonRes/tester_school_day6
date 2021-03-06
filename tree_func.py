"""Module for funny string manipulations"""

from random import randint

def bubbleize(text):
    """Returnes bubbleized string.

    Args:
        text: text to bubbleize
    Return:
        bubbleized text
    """
    chars = []
    for idx, char in enumerate(text):
        if idx % 2:
            chars.append(char.upper())
        else:
            chars.append(char.lower())
    return ''.join(chars)


def randomize(text):
    """Returnes randomized string.

    Args:
        text: text to randomized
    Return:
        randomized text
    """
    chars = []
    for idx, char in enumerate(text):
        if randint(0, 1):
            chars.append(char.upper())
        else:
            chars.append(char.lower())
    return ''.join(chars)


def numberize (text):
    """Returnes numberized string.

    Args:
        text: text to numberized
    Return:
        numberized text
    """
    chars = []
    for idx, char in enumerate(text):
        if char == '3':
            chars.append('!')
        elif char == '2':
            chars.append('@')
        else:
            chars.append(char)
    return ''.join(chars)