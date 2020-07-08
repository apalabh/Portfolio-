def getlist() : 
    l=eval(input("Enter list of numbers : "))
    return l 


def bubblesort(l) :
    flag = 0
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    flag = 1
    return flag

def showList(l, flag=0):
    if flag == 0:
        print(f'The unsorted list is {l}')
    else:
        print(f'The sorted list is {l}')



if __name__ == "__main__":
    l=getlist()
    showList(l)
    flag = bubblesort(l)
    showList(l,flag)