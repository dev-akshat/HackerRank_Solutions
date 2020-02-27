def sockMerchant(n, ar):
    count = 0
    colors = set(ar)
    for color in colors:
        count += ar.count(color) // 2
    return count


a = [1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8]
print(sockMerchant(len(a), a))
