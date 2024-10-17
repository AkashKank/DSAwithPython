
def main():
    print("print odd numbers")

    number = int(input("Enter the number : "))
    sum = 0
    
    for i in range(1, number+1):
        if i%2 != 0:
            print("Odd number : ",i)
            sum+=i
    print("Sum of all odd numbers : ",sum)



if __name__=="__main__":
    main()