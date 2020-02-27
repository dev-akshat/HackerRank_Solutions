def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 1, -1, -1):  # from 4 to 0
        if q[i] - (i + 1) > 2:  # if no - its position is > 2
            print('Too chaotic')
            return
        print(q[i] - 2, ":", i)
        for j in range(max(0, q[i] - 2), i):
            print("yes: j=", q[j], " i=", q[i])
            if q[j] > q[i]:
                bribes += 1
    # print(bribes)
    return bribes


# def minimumBribes(q):
#     count = 0
#     flag = True
#     i = len(q) - 1
#     for x in range(len(q)):
#         temp = max(q) - x
#         index = q.index(temp)
#         if index < i - x:
#             if i - x - index > 2:
#                 print("Too chaotic")
#                 flag = False
#                 break
#             q.remove(temp)
#             q.insert(i - x, temp)
#             count += i - x - index
#     if flag:
#         print(count)

que = [int(s) for s in "2 1 5 3 4".strip().split()]
print("\nBribe=", minimumBribes(que))
