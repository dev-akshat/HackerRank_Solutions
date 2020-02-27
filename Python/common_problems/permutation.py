from itertools import permutations

s, n = input().split()
for x in permutations(sorted(s), int(n)):
    print(*x, sep="")

[print(*p, sep="") for p in permutations(sorted(s), int(n))]
