def designer_mat1(val, sep, txt):
    c = sep
    t = txt
    for i in range(m // n):
        print((c * i).rjust(n + 2, "-") + c + (c * i).ljust(n + 2, "-"))
    print("".rjust(n, "-") + t + "".ljust(n, "-"))
    for i in range(m // n - 1, -1, -1):
        print((c * i).rjust(n + 2, "-") + c + (c * i).ljust(n + 2, "-"))


def designer_mat2(val, sep, txt):
    c = sep
    t = txt
    N, M = map(int, val.split())
    for i in range(1, N, 2):
        print((c * i).center(M, '-'))
    print(t.center(M, '-'))
    for i in range(N - 2, -1, -2):
        print((c * i).center(M, '-'))


n = 9
m = 21
c = ".|."
t = "WELCOME"
designer_mat1(f"{n} {m}", c, t)
designer_mat2(f"{n} {m}", c, t)
