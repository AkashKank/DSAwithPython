
def main():
    print("Sum of numbers from 1 to n")

    number = int(input("Enter the Character : "))
    sum = 0
    
    for i in range(1, number+1):
        sum+=i
    
    print(sum)

if __name__=="__main__":
    main()