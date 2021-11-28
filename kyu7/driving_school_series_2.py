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