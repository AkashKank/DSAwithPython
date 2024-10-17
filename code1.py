
def main():
    print("Candidate is age is legal for voting or not")

    value = int(input("Enter age of candiate : "))

    if value >= 18:
        print("Candidate can vote")
    else:
        print("Cnadidate can not vote")
    

if __name__=="__main__":
    main()