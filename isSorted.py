def isSorted(x,y,z):
    if x>y>z or z>y>x:
        return True
    else:
        return False    
            
if __name__ == "__main__":
    l=[]
    x=int(input("Enter a num : "))
    y=int(input("Enter a num : "))
    z=int(input("Enter a num : "))
    print(isSorted(x, y, z))
