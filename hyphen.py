def hyphen(s) :
    words = s.split("-")
    words.sort()
    

    f=open("hyphen.txt","w")
    f.write("-".join(words))
    f.close()

def showfile():
    f=open("hyphen.txt","r")
    for line in f :
        print(line.rstrip())



if __name__ == "__main__":
    s=input("Enter a string : ")
    hyphen(s)
    showfile()

