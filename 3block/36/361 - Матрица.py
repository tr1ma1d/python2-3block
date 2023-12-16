def matrix(*args):
    if len(args) == 0:
        return [[0]]
    elif len(args) == 1:
        if args[0] in (0, 1):
            return [[0]]
        return [[0 for _ in range(args[0])] for _ in range(args[0])]
    elif len(args) == 2:
        return [[0 for _ in range(args[0])] for _ in range(args[1])]
    elif len(args) == 3:
        return [[args[2] for _ in range(args[0])] for _ in range(args[1])]


rows = matrix()
for row in rows:
    print(*row)
