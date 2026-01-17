# Another sorting method, the counting sort, does not require comparison.
# Instead, you create an integer array whose index range covers the entire range of
# values in your array to sort. Each time a value occurs in the original array, you
# increment the counter at that index. At the end, run through your counting array,
# printing the value of each non-zero valued index that number of times.


def countingSort(arr):
    freq_arr = [0] * 100

    for item in arr:
        freq_arr[item] = freq_arr[item] + 1

    return freq_arr


if __name__ == "__main__":
    countingSort([])
