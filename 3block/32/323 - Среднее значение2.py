test_string = '''
qwerty
1234
password
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


def average(value):
    if len(value) == 0:
        return 0
    else:
        return sum(value) / len(value)


print(average([-5, 2]))
