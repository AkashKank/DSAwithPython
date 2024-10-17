
def main():
    print("Find Character is Uppercase or Lowercase")

    character = str(input("Enter the Character : "))
    stringnum = ord(character)
    
    if stringnum >= 65 and stringnum <= 90:
        print("Given Character is UPPPERCASE")
    else:
        print("Given Character is lowercase")

if __name__=="__main__":
    main()