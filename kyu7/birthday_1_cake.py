def cake(candles, debris):
    deb = [ord(c) for c in debris]
    num = []
    for i in deb: 
        if i % 2 == 0:
            num.append(i - 97)
        else:
            num.append(i)
    if sum(num) > candles:
        return 'Fire!'
    else:
        return 'That was close!'
  
print(cake(56, 'abc'))
print(cake(583, 'slhacx'))
    
    # if sum(deb) > candles:
    #     return 'Fire!'
    # else:
    #     return 'That was close!'

# def cake(candles, debris):
#     deb = [ord(c) for c in debris]
#     return 'Fire!' if sum(deb) > candles else 'That was close!'  

# cake = lambda candles, debris: 'Fire!' if sum([ord(c) for c in debris]) > candles else 'That was close!'

# print(cake(900, 'abcdef'))
# print(cake(56, 'ifkhchlhfd'))

# def cake(candles, debris, num = []):
#     deb = [ord(c) for c in debris]
#     for i in deb: num.append(i - 97 + 1) if i % 2 == 0 else num.append(i) 
#     print(sum(num))
#     return 'Fire!' if sum(num) > candles else 'That was close!'  
  
# print(cake(583, 'slhacx'))
# print(cake(0, 'jpipe'))