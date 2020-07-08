def addNumbers(*args):
    sum = 0
    
    for n in args:
        sum += n
    
    print(sum)


if __name__ == "__main__":
    addNumbers(3,8)
    addNumbers(3,2,9)