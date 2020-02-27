def maximumToys(prices, k):
    count = 0
    for x in sorted(prices):
        k -= x
        if k <= 0:
            break
        count += 1
    return count


a = list(map(int, "1 12 5 111 200 1000 10".split()))
print(maximumToys(a, 50))
