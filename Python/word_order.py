# Word Order


def word_order(a):
    b = {}
    for x in a:
        if b.get(x):
            b[x] += 1
        else:
            b[x] = 1
    c = list(map(str, b.values()))
    print(len(c))
    print(" ".join(c))


def word_order2(a):
    b = {}
    for x in a:
        b.setdefault(x, 0)
        b[x] += 1
    c = list(b.values())
    print(len(c))
    print(*c)


def word_order3(a):
    from collections import Counter, OrderedDict

    class OrderedCounter(Counter, OrderedDict):
        pass

    # d = OrderedCounter(input() for _ in range(int(input())))
    d = OrderedCounter(a)
    print(len(d))
    print(*d.values())


def word_order4(a):
    from collections import OrderedDict
    words = OrderedDict()

    for x in a:
        words.setdefault(x, 0)
        words[x] += 1

    print(len(words))
    print(*words.values())


string = "bcdef abcdefg bcde bcdef".split()
word_order2(string)

## ACTUAL SUBMISSION
# b = {}
# for i in range(int(input())):
#     x = input()
#     b.setdefault(x, 0)
#     b[x] += 1
# c = list(b.values())
# print(len(c))
# print(*c)
