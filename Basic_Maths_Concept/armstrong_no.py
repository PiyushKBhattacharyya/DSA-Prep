def armstrong_no(n):
    sum = 0
    temp = n
    while n > 0:
        ld = n % 10
        n //= 10
        sum = sum*10 + ld*ld*ld
    if temp == sum:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
    

if __name__ == "__main__":
    n = int(input("Enter the digit: "))
    armstrong_no(n)