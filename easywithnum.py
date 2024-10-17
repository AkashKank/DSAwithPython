
def main():
    print("Printing triangel pattern for characters")

    # number = int(input("Enter Number for printimg characters : "))
    # num = 65

    # for i in range(1, number+1):
    #     strnum = chr(num)
    #     for j in range(i):
    #         print(strnum, end="")
    #     num+=1
    #     print()

    number2 = int(input("Enter Number for printimg numbers : "))

    for i in range(1, number2+1):
        for j in range(1, i+1):
            print(j, end="")
        print()


if __name__=="__main__":
    main()