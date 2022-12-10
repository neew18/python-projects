def  no_vowels(my_string: str):
    new_str=""
    for i in my_string:
        if i in "aeiou":
            i=""
        new_str+=i
    return new_str

if __name__=="__main__":
    my_string = "this is an example"
    print(no_vowels(my_string)) #ths s n xmpl
