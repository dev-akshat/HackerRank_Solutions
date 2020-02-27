def countingValleys1(n, s):
    count = 0
    flag = True
    downhill = 0
    for x in s:
        if x is 'U':
            count += 1
        else:
            count -= 1
            if flag:
                downhill += 1
        if count == 0:
            flag = True
        else:
            flag = False
    return downhill

def countingValleys2(n, s):
    count = 0
    flag = True
    downhill = 0
    uphill = 0
    for x in s:
        if x is 'U':
            count += 1
            if flag:
                uphill += 1
        else:
            count -= 1
            if flag:
                downhill += 1
        if count == 0:
            flag = True
        else:
            flag = False
    return count


nn = 8
ss = "UDDUUUDD"
print(countingValleys(nn, ss))
