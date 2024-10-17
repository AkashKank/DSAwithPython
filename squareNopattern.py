
def main():
    print("Star pattern printing")
    # 1234
    # 1234
    # 1234
    # 1234

    number = int(input("Enter a number for stars : "))

    for i in range(1, number+1):
        for j in range(1, number+1):
            print(j ," ", end="")
        
        print()

if __name__=="__main__":
    main()