
def FibonacciSeries(Number):
    n1 = 0
    n2 = 1
    sum = 0

    for i in range(Number):
        print(sum)
        n1 = n2
        n2 = sum
        sum = n1 + n2

def main():
    print("Print Fibonacci Series ")

    Number = int(input("Enter a Number : "))

    if Number <= 0:
        print("Please Enter positive number")
    else:
        FibonacciSeries(Number)

if __name__=="__main__":
    main()