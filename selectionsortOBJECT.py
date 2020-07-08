class SelectionSort(object):
    def __init__(self):
        self.l = eval(input("Enter a list of integers : "))
        self.ssort()

    def ssort(self) :
        for i in range(len(self.l)):
            min = i
            for j in range(i+1,len(self.l)):
                if self.l[min]>self.l[j]:
                    min = j 

            self.l[i],self.l[min]=self.l[min],self.l[i]
        print(self.l)            
if __name__ == "__main__":
    obj = SelectionSort()