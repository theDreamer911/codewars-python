import re


def to_camel_case(text):
    if text == '':
        return ''
    lst = []
    for elem in re.split('-|_', text):
        lst.append(elem)
    lst2 = []
    for i, j in enumerate(lst):
        if i == 0:
            lst2.append(j)
        else:
            lst2.append(j.capitalize())
    return ''.join(lst2)


print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("A-B-C"))


# anter69
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

# SwingKing


def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0] + ''.join([X.capitalize() for x in removed[1:]])


# bse
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)
