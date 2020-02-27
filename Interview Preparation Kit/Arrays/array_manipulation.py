def arrayManipulation1(n, queries):
    arr = [0] * n
    for x in queries:
        a, b, k = x
        for i in range(a - 1, b):
            arr[i] += k
    return max(arr)


def arrayManipulation2(n, queries):
    arr = [0] * n
    for x in queries:
        a, b, k = x
        arr[a - 1:b] = [x + k for x in arr[a - 1:b]]
    return max(arr)


def arrayManipulation3(n, queries):
    from itertools import accumulate

    arr = [0] * (n + 1)
    for x in queries:
        a, b, c = x
        arr[a - 1] += c
        arr[b] -= c
    return max(accumulate(arr))


nn = 5
qq = [
    [int(x) for x in "1 2 100".split()],
    [int(x) for x in "2 5 100".split()],
    [int(x) for x in "3 4 100".split()],
]

print(arrayManipulation1(nn, qq))
print(arrayManipulation2(nn, qq))
print(arrayManipulation3(nn, qq))
