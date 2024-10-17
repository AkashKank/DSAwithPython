
def main():
    print("Star pattern printing")
    # *****
    # *****
    # *****
    # *****
    # *****

    number = int(input("Enter a number for stars : "))

    for i in range(1, number+1):
        for j in range(number):
            print("*", end="")
           
        print()

    
if __name__=="__main__":
    main()