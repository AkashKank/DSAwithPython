
def PrimeFun(Number):
    for i in range(2, Number+1):
        if i % 2 == 0:
            print(i)
        
        # for j in range(i%2 ==0):
        #     print(i)

def main():
    print("Print all Prime Numbers from 2 to N")

    Number = int(input("Enter a Number : "))

    Prm = PrimeFun(Number)

if __name__=="__main__":
    main()