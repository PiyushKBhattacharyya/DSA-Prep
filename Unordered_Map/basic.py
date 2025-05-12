unordered_map = {}

n = int(input('How many items do you want to insert? '))
for i in range(1, n + 1):
    value = int(input(f'Enter value for key{i}: '))
    key = f'key{i}'
    unordered_map[key] = value

key = input('Enter key to access its value (e.g., key1): ')
if key in unordered_map:
    print(f'Value for {key}:', unordered_map[key])
else:
    print(f'Key {key} not found.')

key = input('Enter key to update its value (e.g., key1): ')
if key in unordered_map:
    value = int(input(f'Enter new value for {key}: '))
    unordered_map[key] = value
    print(f'Updated {key} to {value}')
else:
    print(f'Key {key} not found.')


key = input('Enter key to delete (e.g., key1): ')
if key in unordered_map:
    del unordered_map[key]
    print(f'Deleted {key} from the unordered map.')
else:
    print(f'Key {key} not found.')


print('All items in the unordered map:')
for key, value in unordered_map.items():
    print(f'{key}: {value}')