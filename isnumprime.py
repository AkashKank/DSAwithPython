
def main():
    print("Check Number is prime or nots")

    Number = int(input("Enter a number : "))
    sum = 0 
    is_prime = False

    for i in range(2, Number):
        if Number%i == 0:
            print("Factorial of Number : ",i)
            is_prime = True
            # break

    if is_prime == True:
        print("Prime number")
    else:
        print("Not Prime")

if __name__=="__main__":
    main()