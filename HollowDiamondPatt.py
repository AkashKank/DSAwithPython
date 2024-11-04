
def main():
    print("Hollow Diamond Pattern Printing")
    #   *
    #  * *
    # *   *
    #*     * 
    # *   *
    #  * *
    #   *

    Number = int(input("Enter a number for pattern : "))

    for i in range(Number):
        for j in range(1, Number-i):
            # Spaces before pattern
            print(" ", end="")
        # start after spaces
        print("*", end="")
        
        if i != 0:
            for j in range(2*i-1):
                print(" ", end="")
            print("*", end="")
        print()
    
  
    for i in range(Number - 2, -1, -1):
        for j in range(Number - i - 1):
            print(' ', end='')

        # for j in range(1, Number-i):
        #     # Spaces before pattern
        #     print(" ", end="")
        # # star after spaces
        # print("*", end="")

        for j in range(2*i+1):
            if j == 0 or j == 2*i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
   
if __name__=="__main__":
    main()


# for i in range(0, Number):
#         for j in range(Number-i):
#             # Spaces before pattern
#             print(" ", end="")
#         # start after spaces
#         print("*", end="")
        
#         # for k in range(i):
#             # print(" ", end="")
#             # print("*", end="")
#         # print()

#         if i != 0:
#             for j in range(2*i-1):
#                 print(" ", end="")
#             print("*", end="")
#         print()