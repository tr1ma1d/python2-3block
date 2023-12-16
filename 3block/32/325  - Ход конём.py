def checking_cell_format(cell):
    if (65 <= ord(cell[0]) <= 72) and (1 <= int(cell[1]) <= 8):
        return True
    else:
        return False


def cell_to_tuple(cell):
    letters_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    return letters_dict.get(cell[0], 0), int(cell[1])


def to_cell(res_list):
    letters_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    res = []
    for i in range(len(res_list)):
        letter, num = res_list[i]
        res.append(str(letters_dict.get(letter)) + str(num))
    return sorted(res)


def possible_turns(cell):
    if checking_cell_format(cell):
        tuple_cell = cell_to_tuple(cell)
        res = []

        if (tuple_cell[0] + 2 <= 8) and (tuple_cell[1] + 1 <= 8):
            res.append((tuple_cell[0] + 2, tuple_cell[1] + 1))
        if (tuple_cell[0] + 2 <= 8) and (1 <= tuple_cell[1] - 1 <= 8):
            res.append((tuple_cell[0] + 2, tuple_cell[1] - 1))
        if (1 <= tuple_cell[0] - 2 <= 8) and (tuple_cell[1] + 1 <= 8):
            res.append((tuple_cell[0] - 2, tuple_cell[1] + 1))
        if (1 <= tuple_cell[0] - 2 <= 8) and (1 <= tuple_cell[1] - 1 <= 8):
            res.append((tuple_cell[0] - 2, tuple_cell[1] - 1))

        if (tuple_cell[0] + 1 <= 8) and (tuple_cell[1] + 2 <= 8):
            res.append((tuple_cell[0] + 1, tuple_cell[1] + 2))
        if (tuple_cell[0] + 1 <= 8) and (1 <= tuple_cell[1] - 2 <= 8):
            res.append((tuple_cell[0] + 1, tuple_cell[1] - 2))
        if (1 <= tuple_cell[0] - 1 <= 8) and (tuple_cell[1] + 2 <= 8):
            res.append((tuple_cell[0] - 1, tuple_cell[1] + 2))
        if (1 <= tuple_cell[0] - 1 <= 8) and (1 <= tuple_cell[1] - 2 <= 8):
            res.append((tuple_cell[0] - 1, tuple_cell[1] - 2))

        return to_cell(res)
    else:
        print("Неверный формат")


print(possible_turns("H8"))
