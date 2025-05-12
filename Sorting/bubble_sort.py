def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    example = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", example)
    sorted_arr = bubble_sort(example.copy())
    print("Sorted array:", sorted_arr)
