# def minimumSwaps(arr):
#     swaps = 0
#     for i in range(len(arr)):
#         if arr[i] != i + 1:
#             temp = arr.index(i + 1)
#             arr[i], arr[temp] = arr[temp], arr[i]
#             swaps += 1
#     return swaps


def minimumSwaps(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(n)}
    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans


s_arr = "2 3 4 1 5"
ar = [int(x) for x in s_arr.strip().split()]
print("Swaps: ", minimumSwaps(ar))
