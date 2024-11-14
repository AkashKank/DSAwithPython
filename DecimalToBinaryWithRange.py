
def decToBinary(decNum):
    ans = 0
    power = 1

    while decNum > 0:
        rem = decNum % 2
        decNum //= 2
        ans += (rem * power)
        power *= 10

    return ans # Binary Form returned

def main():
    print("Convert a Number Decimal to Binary")
    
    for i in range(1, 10+1):
        print("Decimal to Binary of ",i,":", decToBinary(i))

if __name__=="__main__":
    main()