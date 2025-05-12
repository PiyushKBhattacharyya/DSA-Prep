arr = list(map(int, input('Enter integers separated by space: ').split()))

num = int(input('Enter the number to search: '))

hash_map = {}
for val in arr:
    hash_map[val] = True

if num in hash_map:
    print(f'{num} is present in the array.')
else:
    print(f'{num} is NOT present in the array.')