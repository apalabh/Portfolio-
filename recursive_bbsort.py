def rec_bbsort(l):
    ctr=0
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            ctr+=1
    if ctr==0:
        return l
    else:
        return rec_bbsort(l)

if __name__ == "__main__":
    l=eval(input("Enter a list: ")) 
    print("Sorted list is ",rec_bbsort(l))           
