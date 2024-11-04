
def main():
    print("Butterfly Pattern Printing")
    # *      *
    # **    **
    # ***  ***
    # ********
    # ********
    # ***  ***
    # **    **
    # *      *
    Number = int(input("Enter a number for pattern : "))

    for i in range(1, Number+1):
        for j in range(i):
            print("*",end="")

        for j in range(Number-i):
            print(" ", end="")
        
        for j in range(Number-i):
            print(" ", end="")

        for j in range(i):
            print("*",end="")
        print()
    
    for i in range(Number):
        for i in range(Number-i):
            print("*", end="")

        for j in range(1, Number-i):
            print(" ", end="")

        for j in range(1, Number-i):
            print(" ", end="")
        
        for j in range(i+1):
            print("*",end="")
        print()
        
if __name__=="__main__":
    main()