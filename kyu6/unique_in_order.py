from itertools import groupby


def unique_in_order(text):
    new_text = []
    for diff in text:
        if len(new_text) < 1 or not diff == new_text[len(new_text) - 1]:
            new_text.append(diff)
    return new_text


print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))


# unique_in_order = lambda l: [z for i, z in enumerate(l) if i==0 or l[i-1] != z]


def unique_in_order(iterate):
    return [x for(x, _) in groupby(iterate)]


print(unique_in_order('AAAABBBCCDAABBB'))
