def rec_add(l):
    if len(l)==1:
        return l[0]
    else:
        return l[0]+ rec_add(l[1:])


if __name__ == "__main__":
    l=eval(input("Enter a list of integers : "))
    print("Sum of elements is ", rec_add(l))            