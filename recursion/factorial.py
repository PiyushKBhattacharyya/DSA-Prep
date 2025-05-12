def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(f"Factorial of {n} is {factorial(n)}")