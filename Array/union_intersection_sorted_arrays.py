# Union and Intersection of Two Sorted Arrays - Brute Force, Better, and Optimal Solutions

# Brute Force
# Concept: Use set to get union and intersection, then sort the result.
# T.C: O((n+m)log(n+m))
def union_brute_force(arr1, arr2):
    return sorted(list(set(arr1) | set(arr2)))
def intersection_brute_force(arr1, arr2):
    return sorted(list(set(arr1) & set(arr2)))

# Better
# Concept: Use two pointers to merge arrays for union and intersection.
# T.C: O(n + m)
def union_better(arr1, arr2):
    i, j = 0, 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not res or res[-1] != arr2[j]:
                res.append(arr2[j])
            j += 1
        else:
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
            j += 1
    while i < len(arr1):
        if not res or res[-1] != arr1[i]:
            res.append(arr1[i])
        i += 1
    while j < len(arr2):
        if not res or res[-1] != arr2[j]:
            res.append(arr2[j])
        j += 1
    return res

def intersection_better(arr1, arr2):
    i, j = 0, 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
            j += 1
    return res

# Optimal
# Concept: Same as better for sorted arrays; two pointers is optimal.
# T.C: O(n + m)
# (No further optimization possible for sorted arrays)
# Reuse better solution as optimal.
union_optimal = union_better
intersection_optimal = intersection_better

# Example usage
if __name__ == "__main__":
    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 3, 5, 6]
    print("Union Brute Force:", union_brute_force(arr1, arr2))
    print("Intersection Brute Force:", intersection_brute_force(arr1, arr2))
    print("Union Better/Optimal:", union_better(arr1, arr2))
    print("Intersection Better/Optimal:", intersection_better(arr1, arr2)) 