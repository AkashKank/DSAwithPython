
def main():
    print("Printing Inverted Triangle pattern")
    # 1111
    #  222
    #   33
    #    4

    number = int(input("Enter Number for printimg Inverted Triangle pattern : "))

    for i in range(number):
        for j in range(i):
            print(" ", end="")

        for j in range(number-1,i-1, -1):
            print(i+1, end="")

        print()




if __name__=="__main__":

    main()