
def main():
    print("Character pattern printing")
    # ABCD
    # EFGH
    # IJKL
    # MNOP

    number = int(input("Enter a number for characters : "))
    character = 65

    for i in range(1, number+1):
        for j in range(1, number+1):
            stringnum = chr(character)
            print(stringnum, "", end="")
            character+=1
        print()


    # for i in range(1, number+1):
    #     character = 65
    #     for j in range(number):
    #         stringnum = chr(character)
    #         print(stringnum, " ", end="")
    #         character+=1
    #     print()


if __name__=="__main__":
    main()