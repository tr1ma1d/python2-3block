def from_string_to_list(string, container):
    return container.extend(map(int, string.split()))


a = [1, 2, 3]
from_string_to_list("1 3 99 52", a)
print(*a)

