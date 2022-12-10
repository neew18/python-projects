def histogram(word):
    alphabets= {}
    for alphabet in word:
        if alphabet not in alphabets:
            alphabets[alphabet] = 0
        alphabets[alphabet]+=1

    for key, value in alphabets.items():
        stars = value*"*"
        print(f"{key} {stars}")
    
if __name__=="__main__":
    word = "abba"
    result = histogram(word)