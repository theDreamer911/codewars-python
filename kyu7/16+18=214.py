def add(a, b):
    c = [int(num) for num in str(a)] 
    d = [int(num) for num in str(b)]

    if len(c) < len(d):
        length = len(d) - len(c)
        a = '0' * length + str(a)

    if len(d) < len(c):
        length = len(c) - len(d)
        b = '0' * length + str(b)

    c = [int(num) for num in str(a)] 
    d = [int(num) for num in str(b)]

    z = []
    for x,i in zip(c,d):
        y = x+i
        z.append(str(y))

    return int(''.join(z))

###### ONE LINER #######
def add(a,b):
    return int(str(add(a//10, b//10))+str(a%10+b%10)) if a * b else a + b

###### BEST SOLUTION ######
def add(a,b):
    s = ""
    while a+b:
        a,p = divmod(a,10)
        b,q = divmod(b,10)
        s = str(p+q)+s
    return int(s or '0')

###### UNIQUE #######
def add(*args):
    a, b = map(str, sorted(args))
    a = a.zfill(len(b))
    result = [int(x) + int(y) for x, y in zip(a,b)]
    return int("".join(map(str, result)))