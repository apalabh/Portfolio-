def message(text):
        return text + "Apala"

def display(fun):  # formal parameter
    result = fun("Hello ")
    return(result)


if __name__ == "__main__":
    print(display(message))  # actual parameter
    

   