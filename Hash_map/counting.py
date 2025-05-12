def count_instances(arr, num):
    freq = {}
    for val in arr:
        freq[val] = freq.get(val, 0) + 1
    return freq.get(num, 0)

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    num = int(input("Enter the number to count: "))
    count = count_instances(arr, num)
    print(f"Number of instances of {num}: {count}")
