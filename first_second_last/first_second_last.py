def first_word(sentence):
    first_word = sentence.split(" ")[0]
    return first_word

def second_word(sentence):
    second_word =sentence.split(" ")[1] 
    return second_word

def last_word(sentence):
    last_word = sentence.split( " ")[-1]
    return last_word

if __name__ == "__main__":
    sentence = "it was"
    print(second_word(sentence)) # was
    print(last_word(sentence)) # was