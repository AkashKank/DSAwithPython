
def main():
    print("print odd numbers")

    number = int(input("Enter the number : "))
    
    for i in range(1, number+1):
        if i%2 != 0:
            print("Odd number : ",i)
        else:
            print("Even number : ",i)


if __name__=="__main__":
    main()