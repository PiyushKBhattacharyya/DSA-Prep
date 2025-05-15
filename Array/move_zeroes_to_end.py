# Move Zeroes to End - Brute Force, Better, and Optimal Solutions

# Brute Force
# Concept: Create a new array, add non-zero elements, then zeroes.
# T.C: O(n), Space: O(n)
def move_zeroes_brute_force(arr):
    res = [x for x in arr if x != 0]
    res += [0] * (len(arr) - len(res))
    return res

# Better
# Concept: Count zeroes, shift non-zero elements forward, then fill zeroes at the end.
# T.C: O(n), Space: O(1) (if allowed to modify in-place)
def move_zeroes_better(arr):
    arr = arr[:]
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < n:
        arr[count] = 0
        count += 1
    return arr

# Optimal
# Concept: Use two pointers, swap non-zero with zero in-place.
# T.C: O(n), Space: O(1)
def move_zeroes_optimal(arr):
    arr = arr[:]
    n = len(arr)
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr

# Example usage
if __name__ == "__main__":
    arr = [1, 0, 3, 12]
    print("Brute Force:", move_zeroes_brute_force(arr))
    print("Better:", move_zeroes_better(arr))
    print("Optimal:", move_zeroes_optimal(arr)) 