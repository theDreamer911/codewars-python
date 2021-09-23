def pig_it(text):
    word = text.split(' ')
    txt = [nest[1:] + nest[0] if "?" in nest[0] else nest[1:] + nest[0]
           if "!" in nest[0] else nest[1:] + nest[0] + 'ay' for nest in word]
    return ' '.join(txt)


print(pig_it('Pig latin is cool !'))  # igPay atinlay siay oolcay
