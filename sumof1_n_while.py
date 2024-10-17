
def main():
    print("Sum of numbers from 1 to n")

    number = int(input("Enter the number : "))
    sum = 0
    
    num = 1
    while num <= number:
        sum = sum + num

        # if num == 3:
        #     break

        num+=1

    print(sum)

if __name__=="__main__":
    main()