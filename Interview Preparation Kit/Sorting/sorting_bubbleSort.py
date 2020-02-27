def countSwaps(a):
    n = len(a)
    i = 0
    count = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
            j += 1
        i += 1
    print("Array is sorted in", count, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n - 1])


a1 = list(map(int, "1 2 3".split()))
a2 = list(map(int, "3 2 1 5 4 7 6".split()))
countSwaps(a2)
