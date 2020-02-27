def ifInStringForm(A):
    for arr_i in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        A.append(arr_t)
        return A


def hourglassSum(A):
    # A = ifInStringForm(A)
    smax = -9 * 7
    for row in range(len(A) - 2):
        for column in range(len(A[row]) - 2):
            tl = A[row][column]
            tc = A[row][column + 1]
            tr = A[row][column + 2]
            mc = A[row + 1][column + 1]
            bl = A[row + 2][column]
            bc = A[row + 2][column + 1]
            br = A[row + 2][column + 2]
            s = tl + tc + tr + mc + bl + bc + br
            smax = max(s, smax)
    return smax


my_ar = [[1, 1, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

print(hourglassSum(my_ar))
