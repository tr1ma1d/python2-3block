import sys


def average_height(h_l):
    return sum(h_l) / len(h_l) if h_l else -1


print(average_height([130, 127, 131]))
# print(average_height(list(map(int, sys.stdin))))
