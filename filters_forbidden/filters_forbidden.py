def filter_forbidden(string: str, forbidden: str):
    l=[i for a in list(string) for i in a if i not in forbidden] 
    return "".join(l)

if __name__=="__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)