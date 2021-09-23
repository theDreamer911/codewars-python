# Tribute to Peter-Liang

# def permutations(string):
#     result = set([string])
#     if len(string) == 2:
#         result.add(string[1] + string[0])

#     elif len(string) > 2:
#         for idx, num in enumerate(string):
#             for s in permutations(string[:idx] + string[idx+1:]):
#                 result.add(num + s)

#     return list(result)


# Tribute to rffrancon, sicknick323, temp lolololol

import itertools


def permutations(string):
    return set(''.join(x) for x in itertools.permutations(string, r=len(string)))


# Tribute to Sebek, maxx_d2


def permutations(s):
    if len(s) == 0:
        return []

    elif len(s) == 1:
        return[s]

    else:
        return set(s[i]+p for i in range(len(s)) for p in permutations(s[:i] + s[i+1:]))


print(permutations('aabb'))
