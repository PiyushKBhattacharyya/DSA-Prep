def extract_digit(n):
    digits = []
    while n > 0:
        ld = n % 10
        digits.append(ld)
        n //= 10
    
    print(f"The digits of the number {n} are {digits[::-1]}")
    
if __name__ == "__main__":
    n = int(input("Enter the digit: "))
    extract_digit(n)