# Second Largest in Array - Brute Force, Better, and Optimal Solutions

# Brute Force
# Concept: Compare each element with every other element, skipping the largest, to find the second largest.
# T.C: O(n^2)
def second_largest_brute_force(arr):
    if not arr or len(arr) < 2:
        return None
    largest = max(arr)
    second = None
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] != largest:
                if second is None or arr[j] > second:
                    second = arr[j]
    return second

# Better
# Concept: Use set to remove duplicates, sort, and pick the second last element.
# T.C: O(n log n)
def second_largest_better(arr):
    if not arr or len(arr) < 2:
        return None
    arr_sorted = sorted(set(arr))
    if len(arr_sorted) < 2:
        return None
    return arr_sorted[-2]

# Optimal
# Concept: Traverse the array once, keeping track of the largest and second largest.
# T.C: O(n)
def second_largest_optimal(arr):
    if not arr or len(arr) < 2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

# Example usage
if __name__ == "__main__":
    arr = [2, 5, 1, 3, 9, 7, 9]
    print("Brute Force:", second_largest_brute_force(arr))
    print("Better:", second_largest_better(arr))
    print("Optimal:", second_largest_optimal(arr)) 