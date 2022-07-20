def count_by(x, n):
    l = []
    x_ap = x
    for i in range(n):
        l.append(x)
        x += x_ap
    return(l)


print(count_by(100, 5))