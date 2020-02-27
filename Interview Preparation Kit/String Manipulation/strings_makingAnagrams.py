from collections import Counter


def makeAnagram(a, b):
    # if Counter(a) == Counter(b):
    #     return 0
    # print(sorted(Counter(a)), sorted(Counter(b)))
    if sorted(Counter(a).items()) == sorted(Counter(b).items()):
        print("Yes")
    return False


print(makeAnagram('asdfg', 'gffdsa'))
# print(makeAnagram('cde', 'abc'))
