
def main():
    print("Find Character is Uppercase or Lowercase")

    character = str(input("Enter the Character : "))
    
    if character >= "a" and character <="z":
        print("Given Character is lowercase")
    else:
        print("Given Character is UPPERCASE")

if __name__=="__main__":
    main()