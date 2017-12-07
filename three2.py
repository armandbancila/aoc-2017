def f(n):
    inner = [1, 2, 4, 5, 10, 11, 23, 25]
    outer = []
    
    while True:
        innerSide = len(inner) // 4 + 1
        currentOuter = len(outer)
        # first
        if currentOuter == 0:
            outer += [inner[0] + inner[-1]]
        # second
        elif currentOuter == 1:
            outer += [2 * outer[0] + inner[1]]
        # second to last
        elif currentOuter == innerSide * 4 + 2:
            outer += [outer[-1] + outer[0] + inner[-1] + inner[-2]]
        # last one, bottom right
        elif currentOuter == innerSide * 4 + 3:
            outer += [outer[-1] + outer[0] + inner[-1]]
        # corner
        elif (currentOuter + 1) % (innerSide + 1) == 0:
            index = currentOuter - ((currentOuter + 1) // (innerSide + 1)) * 2
            outer += [outer[-1] + inner[index]]
        # before corner
        elif (currentOuter + 1) % (innerSide + 1) == (innerSide):
            index = (currentOuter - 1) - (currentOuter // (innerSide + 1)) * 2
            outer += [outer[-1] + inner[index] + inner[index - 1]]
        # after corner
        elif (currentOuter + 1) % (innerSide + 1) == 1:
            index = (currentOuter - 1) - (currentOuter // (innerSide + 1)) * 2
            outer += [outer[-1] + outer[-2] + inner[index] + inner[index + 1]]
        # on a side
        else:
            index = currentOuter - (currentOuter // (innerSide + 1)) * 2
            outer += [outer[-1] + inner[index] + inner[index - 1] + inner[index - 2]]
        if len(outer) == innerSide * 4 + 4:
            inner = outer
            outer = []
        x = list(filter(lambda x: x >= n, inner))
        if len(x) > 0 and x[0] >= n: return x[0]

print(f(312051))

