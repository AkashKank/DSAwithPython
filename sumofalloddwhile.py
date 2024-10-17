
def main():
    print("Sum of all odd numbers using while")

    Number = int(input("Enter a number : "))
    sum = 0 

    num = 1
    while num <= Number:
        if num % 2 != 0:
            print("Odd Number : ",num)
            
            sum = sum + num
        num+=1

    print("Sum of all odd numbers is : ",sum)

if __name__=="__main__":
    main()