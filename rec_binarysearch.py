def rec_binary(l,low,high,x):
    if low<=high :
        mid = (low + high)//2
        if x == l[mid]:
            return mid
        elif x < l[mid]:
            return rec_binary(l,low,mid-1,x)
        elif x > l[mid] :
            return rec_binary(l,mid+1,high,x)
    else:
        return -1





if __name__ == "__main__":
    l=eval(input("Enter a list: "))
    x=int(input("Enter element to be found: "))
    l.sort()

    r=rec_binary(l,0,len(l)-1,x)

    if r==-1:
        print("element doesn't exist in list.")
    else:
        print("element found at index ",r )
    

    
