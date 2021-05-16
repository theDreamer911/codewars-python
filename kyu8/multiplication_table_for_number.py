# version one
# def multi_table(number):
#     x = []
#     combine = '\n'
#     for i in range(10):
#         x.append(f'{i+1} * {number} = {(i+1)*number}')
#     return combine.join(x)

# version two
def multi_table(number):
    x = []
    for i in range(10):
        x.append(f'{i+1} * {number} = {(i+1)*number}')
    return '\n'.join(x)


print(multi_table(5))
print(multi_table(1))


# # best
# def multi_table(number):
#     return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))
