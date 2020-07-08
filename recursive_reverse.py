def reverse(s):
    if len(s) == 0 :
        return s
    else :
        return reverse(s[1:]) + s[0]

if __name__ == "__main__":
    s=input("Enter a string : ")
    print("Reversed string is ", reverse(s))