test_string = '''
+++>+++++<-.>.>.-.
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


my_str = input('Введите строку: ')
my_list = [0 for _ in range(30_000)]

f = False
s = False

pos = 0
for i in range(len(my_str)):
    cmd = my_str[i]

    if cmd == '[':
        f = True
    elif f and not s and cmd == '-':
        my_list[pos] = 1
    elif cmd == ']':
        s = True
    if f and s:
        f = False
        s = False
    elif cmd == '>':
        pos += 1
    elif cmd == '<':
        pos -= 1
    elif cmd == '+':
        my_list[pos] += 1
    elif cmd == '-':
        my_list[pos] -= 1
    elif cmd == '.':
        print(my_list[pos])

    if my_list[pos] > 255:
        my_list[pos] = 0
    elif my_list[pos] < 0:
        my_list[pos] = 255
