def get_size(w,h,d):
    return [(2*w*h)+(2*w*d)+(2*h*d), w*h*d]

print(get_size(4,2,6))

get_size = lambda w,h,d: [(2*w*h)+(2*w*d)+(2*h*d), w*h*d]

print(get_size(4,2,6))
