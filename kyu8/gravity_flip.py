def flip(text, arr):
    return sorted(arr) if text == 'R' else sorted(arr, reverse=True)


print(flip('L', [3, 2, 1, 2, 5, 6, 7]))

# flip('R', [3, 2, 1, 2])

# Best


def flip(d, a):
    return sorted(a, reverse=d == 'L')
