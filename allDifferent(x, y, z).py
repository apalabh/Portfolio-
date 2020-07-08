def allDifferent(x, y, z):
    if x == y and x == z and y == z :
        return False 
    elif x==y or y==z or x==z:
        return False
    else :  
        return True    

if __name__ == "__main__":
    x=int(input("Enter no : "))            
    y=int(input("Enter no : "))
    z=int(input("Enter no : "))
    print(allDifferent(x,y,z))        