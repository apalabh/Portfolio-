class Palindrome(object):
    def __init__(self,s):
        self.isPalindrome(s) 

    def isPalindrome(self,s) :
        if s == s[::-1] :
            print(s,"is a palindrome.")
        else:
            print(s,"is not a palindrome.") 


if __name__ == "__main__":
    s = input("Enter a string : ")
    palin = Palindrome(s)               
        
