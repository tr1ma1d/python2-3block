def simple_map(transformation, vals):
    return [transformation(num) for num in vals]


values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(*simple_map(operation, values))
