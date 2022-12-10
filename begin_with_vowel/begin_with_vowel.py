def begin_with_vowel(words: list):
    return [x for x in words if x[0].lower()== "a" or x[0].lower()== "e" or x[0].lower()== "i" or x[0].lower()=="o" or x[0].lower()=="u"]
if __name__=="__main__":
    word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)