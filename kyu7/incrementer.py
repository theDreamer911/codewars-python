def incrementer(nums):
    answer = []
    for idx, val in enumerate(nums):
        if (val+(idx+1)) >= 10:
            if (val+(idx+1)) >= 20:
                answer.append(val+(idx+1)-20)
            else:
                answer.append(val+(idx+1)-10)
        else:
            answer.append(val+(idx+1))

    return answer


print(incrementer([2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 10, 11, 12, 12]))

# GREAT ANSWER
def incrementer(nums):
    return [(v+i) % 10 for i,v in enumerate(nums,1)]

# BEST ANSWER
def incrementer(nums):
    for i, num in enumerate(nums):
        nums[i] = (num + i + 1) % 10
    return nums