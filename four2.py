from collections import Counter
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
            freq1 = Counter()
            for l in word:
                freq1[l] += 1
            for anag in other:
                freq2 = Counter()
                for l in anag:
                    freq2[l] += 1
                if freq1 == freq2:
                    flag = 0
                    break
            if flag == 0: break
        count += flag
    return count

text = open("day4input", "r").read()[:-1]

print(f(text))
print(f("abcde fgij"))
print(f("abcde xyz ecdab"))
print(f("a ab abc abd abf abj"))
print(f("iiii oiii ooii oooi oooo"))
print(f("oiii ioii iioi iiio"))

