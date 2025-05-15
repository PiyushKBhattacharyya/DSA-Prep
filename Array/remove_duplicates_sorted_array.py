# Remove Duplicates from Sorted Array - Brute Force, Better, and Optimal Solutions

# Brute Force
# Concept: For each element, check if it already exists in the result list.
# T.C: O(n^2)
def remove_duplicates_brute_force(arr):
    if not arr:
        return []
    result = []
    for i in range(len(arr)):
        found = False
        for j in range(len(result)):
            if arr[i] == result[j]:
                found = True
                break
            if not found:
                result.append(arr[i])
    return result
    

# Better
# Concept: Use dict.fromkeys to remove duplicates while preserving order.
# T.C: O(n)
def remove_duplicates_better(arr):
    if not arr:
        return []
    return list(set(arr))

# Optimal
# Concept: Since the array is sorted, compare each element with the previous one and add only if different.
# T.C: O(n)
def remove_duplicates_optimal(arr):
    if not arr:
        return []
    n = len(arr)
    res = [arr[0]]
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            res.append(arr[i])
    return res

# Example usage
if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    print("Brute Force:", remove_duplicates_brute_force(arr))
    print("Better:", remove_duplicates_better(arr))
    print("Optimal:", remove_duplicates_optimal(arr)) 