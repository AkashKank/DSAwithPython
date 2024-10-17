
def main():
    print("Find Character is Uppercase or Lowercase")

    character = str(input("Enter the Character : "))

    if character >= "A" and character <= "Z":
        print("UPPER")
    else:
        print("lower")

if __name__=="__main__":
    main()