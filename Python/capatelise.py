def solve1(s):
    return ' '.join((word.capitalize() for word in s.strip().split(' ')))


def solve2(s):
    return ' '.join([word.capitalize() for word in s.strip().split(' ')])


from timeit import timeit

# time difference for same output
print(timeit("' '.join((word.capitalize() for word in 'akshat tamrakar'.strip().split(' ')))", number=10000))
print(timeit("' '.join([word.capitalize() for word in 'akshat tamrakar'.strip().split(' ')])", number=10000))
