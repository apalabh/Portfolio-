def middle(string):
    l=len(string)
    if l%2==0:
        return string[(l//2)-1:(l//2)+1:]
    else :
        return string[(l//2)]    

if __name__ == "__main__":
    string=input("Enter a string : ")
    print(middle(string))        