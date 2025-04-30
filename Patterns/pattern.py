def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()      
def pattern2(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()
def pattern3(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end="")
        print()      
def pattern4(n):
    for i in range(n):
        for j in range(i + 1):
            print(i + 1, end="")
        print()
def pattern5(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end="")
        print()      
def pattern6(n):
    for i in range(n):
        for j in range(n + 1 - i):
            print(j + 1, end="")
        print()     
def pattern7(n):
    for i in range(n):
        for j in range(n-i+1):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")
        for z in range(n-i+1):
            print(" ", end="")
        print()
def pattern8(n):
    for i in range(n):
        for j in range(i+2):
            print(" ", end="")
        for k in range(2*n-(2*i+1)):
            print("*", end="")
        for z in range(i+2):
            print(" ", end="")
        print() 
def pattern9(n):
    pattern7(n)
    pattern8(n)
def pattern10(n):
    pattern2(n)
    pattern5(n-1)
if __name__ == "__main__":
    n = int(input("Enter the size of the pattern (n): "))
    pattern10(n)