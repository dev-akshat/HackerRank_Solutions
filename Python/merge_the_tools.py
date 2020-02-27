# remove_suplicates_from_substring


# MAINTAINS ORDER
def merge_the_tools(string, k):
    from collections import OrderedDict
    n = len(string) // k
    start = 0
    for i in range(n):
        s = string[start:start + k:]
        print(
            "".join(
                OrderedDict.fromkeys(s)
            )
        )
        start += k


# DON'T MAINTAIN ORDER
def merge_the_tools2(string, k):
    start = 0
    for i in range(len(string) // k):
        print(
            "".join(
                set(
                    string[start:start + k:]
                )
            )
        )
        start += k


nn = "AABCAAADA"
kk = 3
merge_the_tools(nn, kk)
