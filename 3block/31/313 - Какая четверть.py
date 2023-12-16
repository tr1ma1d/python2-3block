test_string = '''
Зачем тебе это знать?
Хорошо, записывай
Василий Пупкин
Василий 1
Вася1
Вася!
ВАСЯ
Вася
И тебе привет
Михаил?
Михаил
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
        print('I четверть')
    elif xcoord < 0 < ycoord:
        print('II четверть')
    elif xcoord < 0 and ycoord < 0:
        print('III четверть')
    elif ycoord < 0 < xcoord:
        print('IV четверть')


quarter(3, 4)
