def everything_reversed(my_list: list):
    new_list = []
    for i in my_list:
        i = i[::-1]
        new_list.append(i)
    new_list = new_list[::-1]
    return new_list
    
if __name__=="__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list) #['erom eno', 'elpmaxe', 'ereht', 'iH']