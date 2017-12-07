def f(x):
    y = 1
    s = 1
    # loop can probably be replaced by division
    while True:
        if s >= x: break
        y += 2
        s += 4 * (y - 1)
    z = y // 2
    d = s - x
    if (d // z) % 2 == 0:
        return (d // z + 2) * z - d
    else:
        return d - (d // z - 1) * z

print(f(1024)) # should be 31

print(f(312051)) # should be 430


