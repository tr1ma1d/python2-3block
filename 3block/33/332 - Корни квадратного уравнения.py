test_string = '''
-2.5
1
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


def smaller_root(p, q):
    d = discriminant(1, p, q)
    return (-p - d ** 0.5) / 2


def larger_root(p, q):
    d = discriminant(1, p, q)
    return (-p + d ** 0.5) / 2


def discriminant(a, b, c):
    return b**2 - 4*a*c


def main():
    p = float(input('Введите число (b):'))
    q = int(input('Введите число (c):'))
    print(larger_root(p, q))
    print(smaller_root(p, q))
    print(discriminant(1, p, q))


main()
