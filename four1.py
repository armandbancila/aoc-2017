def f(x):
    # passphrase consists of a series of words separated by ' '
    # should not contain duplicates
    lines = x.split('\n')
    count = 0
    for line in lines:
        words = line.split(" ")
        flag = 1
        for word in words:
            other = words[:]
            other.remove(word)
            if word in other:
                flag = 0
                break
        count += flag
    return count

text = open("day4input", "r").read()[:-1]

print(f(text))
print(f("aa bb cc dd ee"))
print(f("aa bb cc dd aa"))
print(f("aa bb cc dd aaa"))

