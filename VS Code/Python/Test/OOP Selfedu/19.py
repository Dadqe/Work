def a(start=0.0, stop=0.0, step=1.0):
    start = start
    stop = stop
    step = step
    value = start - step
    
    print(start)
    print(stop)
    print(step)
    print(value)
    
    if value + step < stop:
        value += step
        print(value)
    
    print(value)

a(0, 2, 0.5)

