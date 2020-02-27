# def twoStrings(s1, s2):
#     for x in s1:
#         if s2.find(x) == -1:
#             continue
#         return "YES"
#     return "NO"


# def twoStrings(s1, s2):
#     for x in s1:
#         if x not in s2:
#             continue
#         return "YES"
#     return "NO"


def twoStrings(s1, s2):
    for x in s1:
        if x in s2:
            return "YES"
    return "NO"


a1 = "hello"
b1 = "world"
a2 = "hi"
b2 = "world"
print(twoStrings(a1, b1))
print(twoStrings(a2, b2))
