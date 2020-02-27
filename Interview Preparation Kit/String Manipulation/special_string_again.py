from itertools import combinations, groupby
from collections import Counter


def substrCount(n, s):
    l = [(ch, len(list(g))) for ch, g in groupby(s)]
    ans = 0
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])
    return ans


def substrCount1(n, s):
    tot = 0
    count_sequence = 0
    prev = ''
    for i, v in enumerate(s):
        count_sequence += 1
        if i and (prev != v):
            j = 1
            while ((i - j) >= 0) and ((i + j) < len(s)) and j <= count_sequence:
                if s[i - j] == prev == s[i + j]:
                    tot += 1
                    j += 1
                else:
                    break
            count_sequence = 1
        tot += count_sequence
        prev = v
    return tot


def substrCount2(n, s):
    l = []
    count = 0
    cur = None
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))
    ans = 0
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])
    return ans


# TIMEOUT
def substrCount3(n, s):
    count = 0
    for x in (s[x:y]
              for x, y in combinations(range(n + 1), r=2)
              ):
        if x == x[::-1] and len(Counter(x)) <= 2:
            count += 1
    return count


s1 = "asasd"
n1 = len(s1)
s2 = "abcbaba"
n2 = len(s2)
s3 = "aaaa"
n3 = len(s3)

print(substrCount1(n1, s1), substrCount2(n1, s1), substrCount3(n1, s1))  # 7
print(substrCount1(n2, s2), substrCount2(n2, s2), substrCount3(n2, s2))  # 10
print(substrCount1(n3, s3), substrCount2(n3, s3), substrCount3(n3, s3))  # 10
