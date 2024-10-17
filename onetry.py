
def main():
    print("Printing star pattern")

    number = int(input("Enter Number for printimg stars : "))

    for i in range(1, number+1):
        for j in range(i):
            print("*", end="")
        print()



if __name__=="__main__":
    main()