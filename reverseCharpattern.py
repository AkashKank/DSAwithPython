
def main():
    print("Printing reverse character pattern")
    # A
    # CD
    # FDE 
    # JIHG

    number = int(input("Enter Number for printimg reverrse character pattern : "))
    # characterfluid = 65

    for i in range(number):
        for j in range(i, -1, -1):
            print(chr(65 + j), end="")
        print()

    # for i in range(1, number+1):
    #     characterfluid = 65
    #     for j in range(i,0, -1):
    #         convchar = chr(characterfluid)
    #         print(convchar, end="")
    #         characterfluid+=1
    #     print()

  
    # for i in range(number, 0, -1):
    #     characterfluid = 65
    #     for j in range(i):
    #         convchar = chr(characterfluid)
    #         print(convchar, end="")
    #         characterfluid+=1
    #     print()


if __name__=="__main__":

    main()