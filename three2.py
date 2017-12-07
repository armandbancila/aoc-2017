def f(n):
    inner = [1, 2, 4, 5, 10, 11, 23, 25]
    side = lambda x: x // 4 + 1
    get = lambda x, y: x[y] if y < len(x) else x[y % (len(x) - 1)]
    innerSide = side(len(inner))
    outer = []
    
    for i in range(n):
        innerSide = side(len(inner))
        if len(outer) == 0:
            outer += [inner[0] + inner[-1]]
        elif len(outer) == 1:
            outer += [2 * outer[0] + inner[1]]
        # second to last
        elif len(outer) == innerSide * 4 + 2:
            outer += [outer[-1] + outer[0] + inner[-1] + inner[-2]]
        # last one, bottom right
        elif len(outer) == innerSide * 4 + 3:
            outer += [outer[-1] + outer[0] + inner[-1]]
        # corner
        elif (len(outer) + 1) % (innerSide + 1) == 0:
            index = len(outer) - ((len(outer) + 1) // (innerSide + 1)) * 2
            outer += [outer[-1] + inner[index]]
        # before corner
        elif (len(outer) + 1) % (innerSide + 1) == (innerSide):
            index = (len(outer) - 1) - (len(outer) // (innerSide + 1)) * 2
            outer += [outer[-1] + get(inner, index) + get(inner, index - 1)]
        # after corner
        elif (len(outer) + 1) % (innerSide + 1) == 1:
            index = (len(outer) - 1) - (len(outer) // (innerSide + 1)) * 2
            outer += [outer[-1] + outer[-2] + inner[index] + inner[index + 1]]
        # on a side
        else:
            index = len(outer) - (len(outer) // (innerSide + 1)) * 2
            outer += [outer[-1] + get(inner, index) + get(inner, index - 1) + get(inner, index - 2)]
        if len(outer) == side(len(inner)) * 4 + 4:
            inner = outer
            outer = []
    return inner


print(f(1000000))

#print(f(312051))

