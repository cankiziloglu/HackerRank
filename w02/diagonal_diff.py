# You are given a square matrix consisting of integers.\
# You will return the absolute difference between the sums of its diagonals.


def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    n = len(arr)

    for i in range(n):
        sum1 = arr[i][i] + sum1
        sum2 = arr[i][n - i - 1] + sum2

    return abs(sum1 - sum2)
