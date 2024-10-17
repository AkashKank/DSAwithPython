
def main():
    print("Print factorial of number n")

    number = int(input("Enter a number : "))

    for i in range(2, number):
        if number % i == 0:
            print("Factorials : ", i)

if __name__=="__main__":
    main()