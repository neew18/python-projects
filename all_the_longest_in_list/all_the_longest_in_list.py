def all_the_longest(my_list: list):
    list = [] #a new empty list
    maxstring = max(my_list, key=len) #searching for the longest string
    l = len(maxstring) #length of the longest string

    for i in my_list: 
        if len(i) == l : # checking if there are longest strings left or not
            list.append(i) #adding to the new list
            result = list
    return result

if __name__=="__main__":
    
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']