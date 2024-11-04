
def SumOfDigits(num):
   digSum = 0
   while num > 0:
      lastDig = num % 10
      num = num // 10
      digSum = digSum + lastDig

   return digSum

def main():
  print("Print the Sum of Digits")

  num = int(input("Enter a Digit for DigitSum : "))
  print("Sum : ",SumOfDigits(num))

 
if __name__=="__main__":
    main()