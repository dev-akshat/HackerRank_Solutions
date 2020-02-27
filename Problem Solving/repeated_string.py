def repeatedString(s, n):
    x = len(s)
    end_str = (s[0: (n % x)]).count('a')
    total = (s.count('a')) * (n // x)
    return end_str + total


my_s = "aba"
no = 10
print(repeatedString(my_s, no))
