from collections import Counter

X = int(input())
n = Counter(list(
    map(
        int,
        input().split()
    )))
s = []
for _ in range(int(input())):
    s.append(
        list(
            map(
                int,
                input().split()
            )
        )
    )
sale = 0
for k, v in s:
    if n[k] > 0:
        sale += v
        n[k] -= 1
print(sale)
