# 3/12
def fly_by(lamps, drone):
    return lamps.replace('x', 'o', drone.index('T') + 1)

# 4/12
fly_by = lambda lamps, drone: lamps.replace("x", "o", len(drone))

print(fly_by('xxxxxx', '====T'))