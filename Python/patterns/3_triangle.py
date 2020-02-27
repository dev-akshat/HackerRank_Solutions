n = 6
for i in range(0, n):
    for j in range(0, i):
        if i != n - 1:
            if j == 0:
                for k in range(0, n - i):
                    print("", end=" ")
            elif j == i - 1:
                for k in range(0, j):
                    print("", end=" ")
            else:
                print("", end=" ")
                continue
            print("x", end="")
        else:
            if j == 0:
                print("", end=" ")
            print("x", end=" ")
    print()
