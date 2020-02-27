def activityNotifications(expenditure, d):
    count = 0
    m = d // 2
    for i in range(d, len(expenditure)):
        if expenditure[i] >= 2 * sorted(expenditure[i - d:i])[m]:
            count += 1
    return count


def activityNotifications_1(expenditure, d):
    from statistics import median
    count = 0
    for i in range(d, len(expenditure)):
        if expenditure[i] >= 2 * median(expenditure[i - d:i]):
            count += 1
    return count


def activityNotifications_2(expenditure, d):
    from numpy import median
    count = 0
    for i in range(d, len(expenditure)):
        if expenditure[i] >= 2 * median(expenditure[i - d:i]):
            count += 1
    return count


l1 = [10, 20, 30, 40, 50]
l2 = [int(x) for x in "2 3 4 2 3 6 8 4 5".split()]
l3 = [int(x) for x in "1 2 3 4 4".split()]
print("Notifications: ", activityNotifications_1(l1, 3))
