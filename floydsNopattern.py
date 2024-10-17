
def main():
    print("Printing floyd's number pattern")
    # 1
    # 23
    # 456
    # 78910

    number = int(input("Enter Number for printimg floyd's number pattern : "))
    num = 1

    for i in range(1, number+1):
        for j in range(i):
            print(num, end="")
            num+=1
        print()


if __name__=="__main__":

    main()