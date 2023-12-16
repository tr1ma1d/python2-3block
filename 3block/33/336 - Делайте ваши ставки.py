horse_list = [i for i in range(1, 11)]


def do_bet(horse_num, bet):
    print(f'Лошадь {horse_num}, ставка {bet}')
    if (horse_num in horse_list) and (bet > 0):
        print(f'Ваша ставка в размере {bet} на лошадь {horse_num} принята')
        horse_list.remove(horse_num)
    else:
        print('Что-то пошло не так, попробуйте еще раз')


def main():
    do_bet(1, 10)
    do_bet(1, 100)
    do_bet(2, 0)
    do_bet(2, 200)


main()
