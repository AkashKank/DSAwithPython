
def Factoial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def nCr(n, r):
    fact_n = Factoial(n)
    fact_r = Factoial(r)
    fact_nmr = Factoial(n-r)

    return fact_n // (fact_r * fact_nmr)

def main():
    print("Quoficient of Number")

    n = 6
    r = 3
    # nCr(n,r)
    print("Binomial Quoificient is : ",nCr(n,r))
    
if __name__=="__main__":
    main()