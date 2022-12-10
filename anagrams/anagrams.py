def anagrams(string1, string2):
    if sorted(string1)==sorted(string2):
        return True

    else :
        return False

if __name__=="__main__":
    print(anagrams("tame", "meta")) 
    print(anagrams("tame", "mate")) 
    print(anagrams("tame", "team")) 
    print(anagrams("tabby", "batty")) 
    print(anagrams("python", "java")) 