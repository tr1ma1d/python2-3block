daily_food = [0, 150, 150]


def count_food(days):
    my_sum = 0
    if 1 <= len(days) <= 31:
        for i in days:
            my_sum += daily_food[i-1]

    return my_sum


def main():
    print(count_food([2, 3]))


main()
