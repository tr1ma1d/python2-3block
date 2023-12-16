test_string = '''
11
окорок
петлей
Плетей
рококо
теплей
Тишь
ТОМНО
тонко
тонок
тоном
шить
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt, end='')
    tmp = test_string.pop()
    print(tmp)
    return tmp


n = int(input('Кол-во слов: '))
words = sorted([input().lower() for _ in range(n)], reverse=True)

while words:
    word1 = words.pop()
    print('\n', word1, end=' ')
    word2_list = []
    for word2 in words:
        if sorted(list(word1)) == sorted(list(word2)):
            print(word2, end=' ')
            word2_list.append(word2)

    for el in word2_list:
        words.remove(el)

