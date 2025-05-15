# Rotate Array by K Places - Brute Force, Better, and Optimal Solutions

# Brute Force
# Concept: Rotate one by one, k times.
# T.C: O(n*k)
def rotate_brute_force(arr, k):
    n = len(arr)
    k = k % n if n else 0
    res = arr[:]
    for _ in range(k):
        last = res.pop()
        res.insert(0, last)
    return res

# Better
# Concept: Use extra array to place elements at their new positions.
# T.C: O(n), Space: O(n)
def rotate_better(arr, k):
    n = len(arr)
    k = k % n if n else 0
    res = [0]*n
    for i in range(n):
        res[(i + k) % n] = arr[i]
    return res

# Optimal
# Concept: Move each element to its correct position in cycles, so every element is moved exactly once.
# T.C: O(n), Space: O(1)
def rotate_optimal_cycles(arr, k):
    n = len(arr)
    k = k % n if n else 0
    arr = arr[:]
    count = 0
    start = 0
    while count < n:
        current = start
        prev = arr[start]
        while True:
            next_idx = (current + k) % n
            arr[next_idx], prev = prev, arr[next_idx]
            current = next_idx
            count += 1
            if start == current:
                break
        start += 1
    return arr

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Brute Force:", rotate_brute_force(arr, k))
    print("Better:", rotate_better(arr, k))
    print("Optimal Cycles:", rotate_optimal_cycles(arr, k)) 