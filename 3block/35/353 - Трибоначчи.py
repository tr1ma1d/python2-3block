def tribonacci(n):
    if n in (0, 1):
        return 0
    elif n in (2, 3):
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


print(tribonacci(4))
