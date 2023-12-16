import sys


def gematriya(words):
    return sorted(words, key=lambda word: sum([ord(letter)-(ord('A')+1) for letter in word.upper()]))


print(gematriya(['mother', 'Daddy', 'sIster']))
# print(average_height(list(map(str.strip, sys.stdin))))
