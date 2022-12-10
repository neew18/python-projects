def distinct_numbers(my_list: list):
    ordered=sorted(my_list)
    newlist = []
    for i in ordered:
        if i in newlist :
            continue
        else:
            newlist.append(i)

    return newlist

if __name__=="__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    newlist =distinct_numbers(my_list)
    print(newlist) # [1, 2, 3]