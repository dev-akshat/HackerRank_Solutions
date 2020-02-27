from itertools import combinations
from collections import Counter, defaultdict


# WORKING WITH EXPLANATION
def countTriplets(arr, r):
    # initialize the dictionaries
    r2 = {}
    r3 = {}
    count = 0

    # loop throgh the arr itens
    for k in arr:
        # if k in r3 indicates the triplet already completed,
        # the count need be incremented
        if k in r3:
            count += r3[k]

        # if k in r2, it is the secound number of the triplet,
        # your successor (third element k*r) need be added or incremented in the r3 dict
        # because is a potencial triplet
        if k in r2:
            if k * r in r3:
                r3[k * r] += r2[k]
            else:
                r3[k * r] = r2[k]

        # else, k is the first element of the triplet, so,
        # your seccessor (secound element k*r) need be added or incremented in the r2 dict
        # because is a potencial triplet
        if k * r in r2:
            r2[k * r] += 1
        else:
            r2[k * r] = 1

    return count


# WORKING
def countTriplets1(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k * r] += v2[k]
        v2[k * r] += 1
    return count


# WORKING
def countTriplets2(arr, r):
    r2 = {}
    r3 = {}
    count = 0
    for k in arr:
        if k in r3:
            count += r3[k]
        if k in r2:
            if k * r in r3:
                r3[k * r] += r2[k]
            else:
                r3[k * r] = r2[k]
        if k * r in r2:
            r2[k * r] += 1
        else:
            r2[k * r] = 1
    return count


# WORKING
def countTriplets3(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0
    for v in arr:
        if v in r3:
            count += r3[v]
        if v in r2:
            r3[v * r] += r2[v]
        r2[v * r] += 1
    return count


# TIMEOUT
def countTriplets4(arr, r):
    count = 0
    for x in combinations(arr, 3):
        if x[1] // x[0] == r and x[2] // x[1] == r:
            count += 1
    return count


# TIMEOUT
def countTriplets5(arr, r):
    return sum(
        1 for x in combinations(arr, 3)
        if x[1] // x[0] == r and x[2] // x[1] == r
    )


# TIMEOUT
def countTriplets6(arr, r):
    b = 0
    i = 0
    while i < len(arr) - 2:
        a2 = arr[i + 1:]
        j = 0
        while j < len(a2) - 1:
            a3 = a2[j + 1:]
            k = 0
            while k < len(a3):
                if (a3[k] / a2[j]) == r and (a2[j] / arr[i]) == r:
                    b += 1
                k += 1
            j += 1
        i += 1
    return b


l1 = [int(x) for x in "1 2 2 4".split()]
l2 = [int(x) for x in "1 3 9 9 27 81".split()]
l3 = [int(x) for x in "1 5 5 25 125".split()]

print(countTriplets3(l1, 2))  # 2
# print(countTriplets1(l2, 3), countTriplets2(l2, 3))  # 6
# print(countTriplets1(l3, 5), countTriplets2(l3, 5))  # 4
