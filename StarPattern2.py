
def main():
    print("Star pattern printing")
    # *
    # **
    # ***

    number = int(input("Enter a number for pattern : "))

    for i in range(1, number+1):
        for j in range(i):
            print("*", end="")
        print()
 
if __name__=="__main__":
    main()