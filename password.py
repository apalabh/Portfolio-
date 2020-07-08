def takePass():
    p=input("Enter a password : ")
     
    if checkPass(p)== True :
        pn = input("Enter password again : ")
    else :
        p = input("Enter new password : ")  
    if p == pn :
        pass 
    else :
        p=input("Enter a password : ")
    return p           
        
def checkPass(p): 
    for i in p :
        if i.isupper()== True and len(p)>= 8 and p.isalnum == True :
            return True 
        else :
            return False

if __name__ == "__main__":
    p = takePass()
    checkPass(p)            
        

