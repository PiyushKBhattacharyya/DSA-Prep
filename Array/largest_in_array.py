# Largest in Array - Brute Force, Better, and Optimal Solutions

# Brute Force
# Concept: Compare each element with every other element to find the maximum.
# T.C: O(n^2)
def largest_brute_force(arr):
    if not arr:
        return None
    max_elem = arr[0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > max_elem:
                max_elem = arr[j]
    return max_elem
    
# Better
# Concept: Sort the array and pick the last element.
# T.C: O(n log n)
def largest_better(arr):
    if not arr:
        return None
    arr_sorted = sorted(arr)
    return arr_sorted[-1]

# Optimal
# Concept: Traverse the array once, keeping track of the maximum.
# T.C: O(n)
def largest_optimal(arr):
    if not arr:
        return None
    max_elem = arr[0]
    for num in arr:
        if num > max_elem:
            max_elem = num
    return max_elem

# Example usage
if __name__ == "__main__":
    arr = [2, 5, 1, 3, 9, 7]
    print("Brute Force:", largest_brute_force(arr))
    print("Better:", largest_better(arr))
    print("Optimal:", largest_optimal(arr)) 