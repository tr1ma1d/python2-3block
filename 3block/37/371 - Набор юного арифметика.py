def arithmetic_operation(operat):
    if operat == '+':
        return lambda x, y: x + y
    elif operat == '-':
        return lambda x, y: x - y
    elif operat == '//':
        return lambda x, y: x // y
    elif operat == '*':
        return lambda x, y: x * y


operation = arithmetic_operation('+')
print(operation(1, 4))
