def getList():
    l=eval(input("Enter a l : "))
    return l 

def findMax(l,i): 
    max_index = i

    for j in range(i,len(l)):
        if l[j] > l[max_index]:
            # maxi = l[j]
            max_index = j
    
    return max_index   

def selectionSort(l):
    flag = 0

    for i in range(len(l)):
        j=findMax(l,i)    
        if j != i:
            l[i],l[j] = l[j],l[i]
        else:
            pass
    
    flag = 1
    
    return l, flag


def showList(l,flag=0):
    if flag == 0:
        print(f'Unsorted list is {l}')
    else:
        print(f'Sorted list is {l}')


if __name__ == "__main__":
    l=getList()
    showList(l)
    l,f = selectionSort(l)
    showList(l,f)
    