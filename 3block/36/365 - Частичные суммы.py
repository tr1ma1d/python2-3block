def partial_sums(*args):
    return [0] + [sum(args[:i+1]) for i in range(len(args))]


print(partial_sums(1, 0.5, 0.25, 0.125))
