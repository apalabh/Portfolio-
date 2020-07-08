def fibo(n):
    a=0
    b=1
    c=0 

    for _ in range(n):
            c=a+b
            a=b
            b=c
            return b
def main():
    n=int(input("Enter a number : ")) 
    print(fibo(n))           

if __name__ == "__main__" :
    main()

