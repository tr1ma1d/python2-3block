import sys


def sort_line(line):
    return sorted(line, key=lambda x: x.lower())


print(sort_line('cats dog CAT DOGGY monkey'.split()))
# print(sort_line(list(map(str.strip, sys.stdin))))
