def character_hashing(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

if __name__ == "__main__":
    input_string = "hello world"
    result = character_hashing(input_string)
    print("Character frequencies:", result)