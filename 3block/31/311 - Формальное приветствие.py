test_string = '''
Иван
Смирнов
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


def greet():
    name = input()
    surname = input()
    print('Hello,', name, surname)


greet()
