def f(l):
    l = list(map(int, l.split("\n")))
    jump = 0
    count = -1
    while True:
        if jump < 0: jump -= 1
        count += 1
        pos = jump
        l[jump] += 1
        jump = l[jump] - 1 + pos
        if jump >= len(l):
            count += 1
            break
    return count

text = open("day5input", "r").read()[:-1]

# print(f(text))
test = """0
3
0
1
-3"""
print(f(test))
print(f(text))
