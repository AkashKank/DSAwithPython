
def main():
    print("Printing reverse number pattern")

    number2 = int(input("Enter Number for printimg reverse number pattern : "))

    for i in range(number2, 0, -1):
        for j in range(i):
            print(i, end="")
        print()


if __name__=="__main__":
    main()