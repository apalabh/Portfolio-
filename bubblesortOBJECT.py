class BubbleSort(object):
    def __init__(self):
        self.getList()

        
    def getList(self) : 
        self.l = eval(input("Enter a list of integers : "))

    def BBsort(self) :
        for i in range(len(self.l)):
            for j in range(len(self.l)-1):
                if self.l[j]>self.l[j+1]:
                    self.l[j] , self.l[j+1] = self.l[j+1],self.l[j]
        print(self.l)


if __name__ == "__main__":
    bsort = BubbleSort()
    bsort.BBsort()                    