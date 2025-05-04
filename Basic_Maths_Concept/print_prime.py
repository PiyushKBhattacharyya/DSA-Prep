def prime(n):
    cnt = 0
    for i in range (1, n + 1):
        if n % i == 0:
            cnt += 1
    if cnt == 2: print(f"{n} is a prime no")
    else: print(f"{n} is not a prime no")

if __name__ == "__main__":
    n = int(input("Enter the digit: "))
    prime(n)