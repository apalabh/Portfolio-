class Account(object):
    def __init__(self,amt,trans):
        self.balance = 67890.00
        self.amt = amt 
        self.trans = trans
        
        
    def bankAcc(self):
        if self.trans == 'w':
            if self.amt < self.balance:
                self.balance -= self.amt 
            else :
                print("ERROR : Amount greater than existing bank balance. ")    
        elif self.trans == 'd' :
            self.balance += self.amt   
        print("Current balance : ",self.balance)      

if __name__ == "__main__":
    trans = input("Do you want to withraw/deposit? Press w or d . ") 
    amt = float(input("Enter amount to be withdrawn/deposited : "))        
    obj = Account(amt,trans)
    obj.bankAcc()