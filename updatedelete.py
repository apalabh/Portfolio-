import sys, os

def closeFile(fin, fout):
    fin.close()
    fout.close()

def ifExists(acc, fin):
    for line in fin:
        if line != '\n':
            if int(line.split(' ', 1)[0]) == int(acc):
                return True
    else: return False

def insertRecord():
    fin = open('accounts.txt', 'r')

    print(f'We are about to insert a new record')
    print(f'Please furnish the following details')
    acc_no = input("Enter the account number you wanna insert: ")
    
    r = ifExists(acc_no, fin) # search for the account number in the accounts.txt file
    
    if r:
        print(f'Sorry account number {acc_no} already exists. Please provide another account number.')
        fin.close()
        return
    else:
        fout = open('accounts.bak', 'a')
        print(f'account number {acc_no} does not exist in the file.')
        name = input("Enter the name of the account holder: ")
        balance = input("Enter the balance amount: ")
        
        # form the record
        record = acc_no + ' ' + name + ' ' + balance + '\n'
        
        # take the file pointer to the beginning
        fin.seek(0, 0)
        
        # write the records with smaller account number than the given one
        for line in fin:
            if int(line.split(' ', 1)[0]) < int(acc_no):
                fout.write(line)

        # now the write the record
        fout.write(record)

        fin.seek(0,0)
        # now the records with greater account number
        for line in fin:
            if int(line.split(' ', 1)[0]) > int(acc_no):
                fout.write(line)
                        
        os.remove('accounts.txt')
        os.rename('accounts.bak', 'accounts.txt')
        
        print(f'record with account number {acc_no} successfully inserted.')
        closeFile(fin, fout)

def delRecord():
    fin = open('accounts.txt')
    acc_no = input(f'Enter the account number to delete:')
    r = ifExists(acc_no, fin)

    if r:
        fout = open('accounts.bak', 'a')
        print(f'Account number {acc_no} exists in the file. We are going to delete it.')
        fin.seek(0,0)

        for line in fin:
            if int(line.split(' ', 1)[0]) != int(acc_no):
                fout.write(line)

        os.remove('accounts.txt')
        os.rename('accounts.bak', 'accounts.txt')

        closeFile(fin, fout)
        print(f'Record of account number {acc_no} deleted successfully.')
    else:
        print(f'No such record found with account number {acc_no}')
        fin.close()


def updateRecord():
    fin = open('accounts.txt')
    print('Enter the account number whose record you wanna update: ')
    acc_no = input()

    r = ifExists(acc_no, fin)

    if r:
        fout = open('accounts.bak', 'a')
        print(f'What do you wanna update, name or balance? ')
        reply = input()
        
        fin.seek(0, 0)

        if reply == 'name':
            new_name = input('Enter new name for the account holder: ')
            for line in fin:
                if int(line.split(' ', 1)[0]) < int(acc_no):
                    fout.write(line)
                elif int(line.split(' ', 1)[0]) == int(acc_no):
                    fout.write(acc_no + " " + new_name + " " + line.rsplit(' ', 1)[1] + '\n')
                elif int(line.split(' ', 1)[0]) > int(acc_no):
                    fout.write(line)
        
        elif reply == 'balance':
            new_balance = input('Enter new blance: ')

            for line in fin:
                if int(line.split(' ', 1)[0]) < int(acc_no):
                    fout.write(line)
                elif int(line.split(' ', 1)[0]) == int(acc_no):
                    fout.write(line.rsplit(' ', 1)[0] + " " + new_balance + "\n")
                elif int(line.split(' ', 1)[0]) > int(acc_no):
                    fout.write(line)
        
        os.remove('accounts.txt')
        os.rename('accounts.bak', 'accounts.txt')

        print(f'record of accont number {acc_no} has been successfully updated.')

        closeFile(fin, fout)
    
    else:
        print(f'No such record found with account number {acc_no}.')
        fin.close()
        

def showAllRecords():
    fin = open('accounts.txt')

    print(f'The records of the accounts file are:')

    line = fin.readline()
    
    if line == '':
        print(f'File is empty.')
        return
        
    while line:
        print(line)
        line = fin.readline()
            
    fin.close()
            
              
if __name__ == "__main__":
    while 1:
        print(f'The options for the user are: ')
        print(f'1: Isert record\n2: Delete record\n3: Update record\n4: Show all records\n5: Exit')
        print(f'Enter your choice: ', end='')
        reply = int(input())

        if reply == 1:
            insertRecord()
        elif reply == 2:
            delRecord()
        elif reply == 3:
            updateRecord()
        elif reply == 4:
            showAllRecords()
        elif reply == 5:
            sys.exit()
        