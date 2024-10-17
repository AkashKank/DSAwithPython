
def main():
    print("Sum of all odd numbers")

    number = int(input("Enter a number : "))
    sum = 0
    
    for i in range(1, number+1):
        if i%2 == 0:
            print("Even Number : ",i)

            sum = sum+i
            # i+=1
    print("Sum of all even numbers : ",sum)


if __name__=="__main__":
    main()