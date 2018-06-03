
def histogram(text):
    hist = {}

    for char in text.lower():
        if char.isalpha():
            hist[char] = hist.get(char, 0) + 1
        else:
            hist['others'] = hist.get('others', 0) + 1
    return hist

print(histogram('costamsprobowacczydziala12jfkjfks2-0jkf;lf'))




