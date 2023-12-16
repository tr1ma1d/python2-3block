items = []
cost = []
a = 0


def add_item(item_name, item_cost):
    items.append(item_name)
    cost.append(int(item_cost))


def print_receipt():
    if items:
        global a
        print('Чек ', a+1, '. Всего предметов: ', len(items), sep='')

        for i in range(len(items)):
            print(items[i], '-', cost[i])

        print('Итого:', sum(cost))
        print('-----')
        items.clear()
        cost.clear()
    else:
        return


def main():
    add_item('Блокнот', 100)
    print_receipt()

    add_item('Ручка', 70)
    print_receipt()
    print_receipt()

    add_item('Булочка', 15)
    add_item('Булочка', 15)
    add_item('Чай', 5)
    print_receipt()

    add_item('Булочка', 15)
    add_item('Булочка', 15)


main()