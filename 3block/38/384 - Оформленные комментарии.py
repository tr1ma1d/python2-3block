import sys


def func(line):
    i, com = line
    return 'Line {}: {}'.format(i, com.lstrip('#').strip())


sys_stdin = '''
import sys
    for line in sys.stdin:
        # rstrip(’\\n’) "отрезает" от строки line,
        # идущий справа символ перевода строки,
        # ведь print сам переводит строку
        print(line.rstrip(’\\n’))
'''[1:-1].split('\n')
user_input = map(str.lstrip, sys_stdin)
filter_input = filter(lambda x: x[1].startswith('#'), enumerate(user_input, 1))
print(*map(func, filter_input), sep='\n')
