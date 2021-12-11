def buy(x, arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                print(i,j)
                if arr[i] + arr[j] == x:
                    return[i,j]


from itertools import combinations

def buy(card, lists):
    return next(([i,j] for (i,x), (j,y) in combinations(enumerate(lists), 2) if x+y==card),None)


def buy(card, arr):
    for i, t in enumerate(arr):
        for i2, t2 in enumerate(arr):
            if i2 == i: continue
            if t+t2 == card:return[i,i2]

print(buy(5,[1,2,3,4,5]))