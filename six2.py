def f(l):
    l = list(map(int, l.split("\t")))
    history = []
    counts = []
    count = 0
    foundAt = 0
    while True:
        history.append(l[:])
        counts.append(count)
        index = l.index(max(l))
        blocks = l[index]
        l[index] = 0
        while blocks > 0:
            index = (index + 1) % (len(l))
            l[index] += 1
            blocks -= 1
        count += 1
        if l in history:
            firstSeen = counts[history.index(l)]
            break
    return count - firstSeen

print(f("0\t2\t7\t0"))
print(f("4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"))

