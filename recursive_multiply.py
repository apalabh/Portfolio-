def product(a,b):
    if a==0 or b==0 :
        return 0
    elif  a==0 and b==0 :
        return 0 
    elif a!=0 and b!= 0 :
        return a + product(a,b-1)      

if __name__ == "__main__":
    a=int(input("Enter a number:"))
    b=int(input("Enter another number:"))
    print(a,'*',b ,'=',product(a,b))