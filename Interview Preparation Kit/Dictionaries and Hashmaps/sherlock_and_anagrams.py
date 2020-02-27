from collections import Counter
from itertools import combinations


def sherlockAndAnagrams1(s):
    count = []
    for i in range(1, len(s) + 1):
        a = ["".join(sorted(s[j:j + i])) for j in range(len(s) - i + 1)]
        b = Counter(a)
        count.append(sum([len(list(combinations(['a'] * b[j], 2))) for j in b]))
    return sum(count)


def sherlockAndAnagrams2(s):
    count = 0
    length = len(s) + 1
    for i in range(1, length):
        a = ("".join(sorted(s[j:j + i])) for j in range(length - i))
        b = Counter(a)
        for j in b:
            count += b[j] * (b[j] - 1) // 2
    return count


def sherlockAndAnagrams3(s):
    n = len(s)
    res = 0
    for l in range(1, n):
        cnt = {}
        for i in range(n - l + 1):
            subs = list(s[i:i + l])
            subs.sort()
            subs = ''.join(subs)
            if subs in cnt:
                cnt[subs] += 1
            else:
                cnt[subs] = 1
            res += cnt[subs] - 1
    return res


print(sherlockAndAnagrams1("ifailuhkqq"),
      sherlockAndAnagrams2("ifailuhkqq"),
      sherlockAndAnagrams3("ifailuhkqq")
      )

print(sherlockAndAnagrams1("abcd"),
      sherlockAndAnagrams2("abcd"),
      sherlockAndAnagrams3("abcd")
      )

print(sherlockAndAnagrams1("abba"),
      sherlockAndAnagrams2("abba"),
      sherlockAndAnagrams3("abba")
      )
