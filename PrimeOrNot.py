
def CheckPrime(Number):
    if Number % 2 == 0:
        return 1
    else:
        return 0

def main():
    print("Print Given Number is Prime or Not")

    Number = int(input("Enter a number : "))

    CheckedNum = CheckPrime(Number)

    if CheckedNum == 1:
        print("Number is Prime")
    else:
        print("Number is Non Prime")

if __name__=="__main__":
    main()