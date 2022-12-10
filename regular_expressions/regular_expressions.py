import re

def is_dotw(my_string: str):
    days="Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    if re.search(days,my_string):
        return True
    return False

def all_vowels(my_string: str):
    for i in my_string:
        if re.search("[aeiou]",i):
            pass
        else:
            return False
    return True

if __name__ == "__main__":
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))

def time_of_day(my_string: str):
    check=False
    string=my_string.split(":")

    if re.search("^(2[0-4]|1[0-9]|[1-9])$",string[0]) and re.search("[0-5][0-9]",string[1]) and re.search("[0-5][0-9]",string[2]):
        check=True
    return check
if __name__ == "__main__":
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))