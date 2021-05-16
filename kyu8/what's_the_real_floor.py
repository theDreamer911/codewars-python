def get_real_floor(n):
    america = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15]
    europa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    return america.index(n)


print(get_real_floor(13))
# print(get_real_floor(5))
# print(get_real_floor(15))
