
def main():
    print("Pattern printing of pyrmid")

    #   1
    #  121
    # 12321
    #1234321

    number = int(input("Enter a number for pattern : "))

    for i in range(number):
        for j in range(i):
            print(i, end="")
        print()

if __name__=="__main__":
    main()