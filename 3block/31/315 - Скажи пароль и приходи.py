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


def ask_password():
    for i in range(3):
        if input('Введите пароль: ') == 'password':
            print('Пароль принят')
        elif i == 2:
            print('В доступе отказано')


ask_password()
