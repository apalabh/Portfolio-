def firstDigit(n) :
    s=str(n)
    return int(s[0])

if __name__ == "__main__":
        n=int(input("Enter a num : "))
        print("The first digit is ", firstDigit(n))