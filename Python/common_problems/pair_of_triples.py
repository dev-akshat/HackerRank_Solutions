a = [0, 1, 2, 3, 4, 5, 6, 7]
b = []
i = 0
while i < len(a) - 2:
    a2 = a[i + 1:]
    j = 0
    while j < len(a2) - 1:
        a3 = a2[j + 1:]
        k = 0
        while k < len(a3):
            b.append([a[i], a2[j], a3[k]])
            k += 1
        j += 1
    i += 1
for x in b:
    print(x)
