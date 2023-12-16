scoring = {'Внешнее_кольцо': {1: 8, 2: 6, 3: 42, 20: 50},
           'Внутреннее_кольцо': {1: 2, 2: 9, 3: 56, 20: 3}}


def score(ring_name, sector_number=0):
    if ring_name == 'Яблочко':
        return 50
    elif ring_name == 'Зелёное кольцо':
        return 25
    elif ring_name == 'Внешнее_кольцо':
        return scoring['Внешнее_кольцо'].get(sector_number)
    elif ring_name == 'Внутреннее_кольцо':
        return scoring['Внутреннее_кольцо'].get(sector_number)


print(score("Яблочко"))
print(score("Внешнее_кольцо", 1))
