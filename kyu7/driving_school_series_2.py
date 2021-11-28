def cost(mins):
    if mins > 5 and mins <= 65:
        return 30
    elif mins > 65:
        price = 30
        mins -= 60

        while (mins > 5):
            price += 10
            mins -= 30
    return price

print(cost(273))

########### BEST SOLUTION ######################
import math

def best(mins):
    return 30 + 10 * math.ceil(max(0, mins - 60 - 5) / 30)


########### ONE LINER ######################
def one_liner(mins):
    return 30 if mins <= 60 else 30 + 10*int((mins - 60 + 24) / 30)

def one_liner_second(mins):
    return max(0, -(-(mins - 65) // 30)) * 10 + 30