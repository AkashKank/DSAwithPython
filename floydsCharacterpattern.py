
def main():
    print("Printing floyd's character pattern")
    # A
    # BC
    # EDF
    # GHIJ

    number = int(input("Enter Number for printimg floyd's character pattern : "))
    characterfluid = 65

    for i in range(1, number+1):
        for j in range(i):
            convchar = chr(characterfluid)
            print(convchar, end="")
            characterfluid+=1
        print()


if __name__=="__main__":

    main()