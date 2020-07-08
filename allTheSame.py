def allTheSame(x,y,z):
    if x == y and x == z and y == z :
        return True 
    else :
        return False


if __name__ == "__main__":
    x=int(input("Enter no : "))            
    y=int(input("Enter no : "))
    z=int(input("Enter no : "))
    print(allTheSame(x,y,z))