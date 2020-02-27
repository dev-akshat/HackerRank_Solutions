from collections import Counter


def checkMagazine1(magazine, note):
    d1 = Counter(magazine)
    for k, v in Counter(note).items():
        if d1[k] < v:
            print("No")
            break
    else:
        print("Yes")


def checkMagazine2(magazine, note):
    print("No") if Counter(note) - Counter(magazine) else print("Yes")


m = "two times three is not four"
m = [x for x in m.strip().split()]
n = "two times two is four"
n = [x for x in n.strip().split()]
checkMagazine1(m, n)
checkMagazine2(m, n)
