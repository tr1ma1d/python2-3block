def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) in (0, 1)


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
