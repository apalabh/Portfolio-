# def readfile():
#     fin = open("accounts.txt", "r")
#     for line in fin :
#         l=line.rsplit(" ",1)[0].split(" ",1)[1] 
#         print(l)
#     fin.close()

# def reverseRecords():
#     f = open("accounts.txt","r")
#     records = f.readlines()
#     records.reverse()
#     for record in records :
#         print(record.rstrip())
#     f.close()    

# def balanceBw() :
#     f= open("accounts.txt","r")
#     for line in f :
#        line = line.rstrip()
#        balance = float(line.rsplit(" ",1)[1])
#        if 5000.00 <= balance <= 8000.00 :
#            print(*line.split(' ',1)[1].rsplit(" ",1)[0])

    # f.close()        

def backupFile() :
    fin = open("accounts.txt","r")
    fout = open("accbackup.txt","w")
    for line in fin :
        line = line.rstrip()
        balance = float(line.rsplit(" ",1)[1])
        if balance < 5000.00 or balance > 8000.00 :
            print(line,file = fout)
    fin.close()
    fout.close()        

if __name__ == "__main__":
   
    backupFile()