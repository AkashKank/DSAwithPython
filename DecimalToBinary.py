
# def decToBinary(decNum):
#     ans = 0
#     power = 1  # Renamed to avoid confusion with the built-in pow() function

#     while decNum > 0:
#         rem = decNum % 2
#         ans += (rem * power)
#         power *= 10
#         decNum //= 2  # Use integer division to update decNum
    
#     return ans  # Binary Form

def decToBinary(decNum):
    ans = 0
    power = 1

    while decNum > 0:
        # rem = decNum % 2
        # ans += (rem * power) 
        # power *= 10
        # decNum /= 2

        rem = decNum % 2
        decNum //= 2
        ans += (rem * power)
        power *= 10

    return ans # BInary Form

def main():
    print("Convert a Number Decimal to Binary")
    
    decNum = int(input("Enter a decmal number : "))

    print("Decimal to Binry of ",decNum,":", decToBinary(decNum))
if __name__=="__main__":
    main()