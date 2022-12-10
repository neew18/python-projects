def length_of_longest(my_list: list):
    count = 0
    for i in my_list:
        if len(i)>count:
            count=len(i)
            result = len (i)
    return result

if __name__=="__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)