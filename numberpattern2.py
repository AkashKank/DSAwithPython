
def main():
    print("numbers pattern printing")
    # 123
    # 456
    # 789

    number = int(input("Enter a number for pattern : "))
    count = 1

    for i in range(1, number+1):
        for j in range(1, number+1):
          print(count, end="")
          count+=1
        print()

    # number = 3
    # for i in range(1, number+1):
    #     character = 65
    #     for j in range(1, number+1):
    #         charstr = chr(character)
    #         print(charstr, end="")
    #         character+=1
    #     print()

    # number = 3
    # character = 65
    # for i in range(1, number+1):
    #     for j in range(1, number+1):
    #         charstr = chr(character)
    #         print(charstr, end="")
    #         character+=1
    #     print()
            
 
if __name__=="__main__":
    main()