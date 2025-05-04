def rev_num(n):
    rev = 0
    temp = n
    while n > 0:
        ld = n % 10
        n //= 10
        rev = rev * 10 + ld
    print(f"Reverse of {temp} is {rev}")

if __name__ == "__main__":
    n = int(input("Enter the digit: "))
    rev_num(n)