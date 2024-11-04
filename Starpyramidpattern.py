
def main():
    print("Star Pyramid Pattern Printing")
    #   *
    #  * *
    # * * *
    #* * * * 

    Number = int(input("Enter a number for pattern : "))

    for i in range(1, Number+1):
        for j in range(Number-i):
            # Spaces before pattern
            print(" ", end="")
        
        for k in range(i):
            print(" ", end="")
            print("*", end="")

        print()

    # for i in range(Number, 0, -1):
    #     for j in range(Number-i):
    #         print(" ", end="")
    #     print()
if __name__=="__main__":
    main()