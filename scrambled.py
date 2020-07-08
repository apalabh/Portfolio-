def scramble(word):
    s=""
    if len(word) <= 3 :
        return word 
    else :
        return (word[0] + word[-2:-len(word):-1] + word[-1])

if __name__ == "__main__":
    sent=input("Enter a sentence : ")
    l=sent.split()
    newsent=""
    for i in l :
        sc = scramble(i)            
        newsent += sc + " "
    print(newsent)            