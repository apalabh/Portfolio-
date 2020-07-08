def isPalendrome(st,start,end):
    if start == end :
        return True
    elif st[start] != st[end]  :
        return False
    elif start < end+1:
        return isPalendrome(st,start+1,end-1)
    else:
        return True         
      
if __name__ == "__main__":
    st=input("Enter string : ")
    st.lower()
    start=0
    end=len(st)-1
    if isPalendrome(st,start,end):
        print("True")
    else :
        print("False")        