from re import findall


def str_to_hash(st):
    if st == '':
        return {}
    else:
        ans = st.split(', ')
        ans2 = []
        label = []
        val = []
        for i in range(len(ans)):
            ans2.append(ans[i].split('='))
        for j in range(len(ans2)):
            label.append(ans2[j][0])
            val.append(int(ans2[j][1]))
        combine = dict(zip(label, val))
        return combine


print(str_to_hash("a=1, b=2, c=3, d=4"))
print(str_to_hash(''))


# sergfsm
def str_to_hash(st):
    return {i: int(j)for i, j in findall(r'(\w+)=(\d+)', st)}

# ejini战神


def str_to_hash(st):
    return {} if not st else {x.split("=")[0]: int(x.split("=")[1]) for x in st.split(", ")}

# Alfinho


def str_to_hash(st):
    result = {}
    if st:
        for i in st.split(', '):
            value = i.split('=')
            result[value[0]] = int(value[1])
    return result


# MrInvincible
def str_to_hash(st):
    d = {}
    if st == '':
        return {}
    for el in st.split(', '):
        one = el.split('=')[0]
        two = el.split('=')[1]
        d[one] = int(two)
    return d
