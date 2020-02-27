def jump(c):
    i = 0
    end = len(c) - 1
    step = 0
    while i < end:
        if ((i + 2) <= end) and (c[i + 2] == 0):
            i += 2
            step += 1
        else:
            i += 1
            step += 1
    return step


clouds = [0, 0, 0, 1, 0, 0]
clouds_2 = [0, 0, 1, 0, 0, 1, 0]
print("3: ", jump(clouds))
print("4: ", jump(clouds_2))
