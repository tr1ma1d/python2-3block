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


def average_value(arr):
    return sum(arr) / len(arr)


def mediana_arr(arr):
    return


def bracket_check(test_str):
    open_brackets = 0
    close_brackets = 0

    for bracket in test_str:
        if bracket == '(':
            open_brackets += 1
        elif bracket == ')':
            close_brackets += 1
        if open_brackets < close_brackets:
            break

    print('YES' if open_brackets == close_brackets else 'NO')


bracket_check('(())')
