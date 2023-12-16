def rec_linear_sum(some_list):
    if not some_list:
        return 0
    return some_list.pop() + rec_linear_sum(some_list)


print(rec_linear_sum([1, 2, 3]))

