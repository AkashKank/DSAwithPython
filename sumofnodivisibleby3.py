
def main():
    print("Print Sum of 1-n numbers which are divisible by 3")

    number = int(input("Enter the number : "))
    sum = 0 

    for i in range(1, number+1):
        if i % 3 == 0:
            print("Numbers which are divisible by 3 : ",i)
            sum = sum+i
    print(sum)
            


if __name__=="__main__":
    main()