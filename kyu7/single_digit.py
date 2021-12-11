to_binary = lambda x: bin(x).replace('0b', '')

def single_digit(n):
    ans = [int(i) for i in to_binary(n)]
    if sum(ans) % 16 == 0:
        ans2 = [int(i) for i in to_binary(sum(ans))]
        return sum(ans2)
    else:
        return sum(ans)

print(single_digit(5665))