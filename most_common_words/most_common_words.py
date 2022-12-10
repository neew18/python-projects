def most_common_words(filename: str, lower_limit: int):
    sent=""
    with open(filename) as file:
        for l in file:
            sent+=l
        s=sent.replace("\n","")
        s=s.replace("."," ")
        s=s.replace(",","")
        s=s.split()
        
    return {x : s.count(x) for x in s if s.count(x) >= lower_limit} 
if __name__=="__main__":   
    print(most_common_words("comprehensions.txt", 3))