
def main():
    print("Check grade by marks")

    marks = int(input("Enter the marks : "))

    if marks >= 90:
        print("A Grade")
    elif marks >= 80 and marks<90:
        print("B Grade")
    elif marks >= 60 and marks<80:
        print("C Grade")
    elif marks >= 35 and marks<60:
        print("Pass")
    else:
        print("fail")
    

if __name__=="__main__":
    main()