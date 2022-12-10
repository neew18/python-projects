class ListHelper:
    @classmethod
    def greatest_frequency(cls,my_list: list):
        list_dict= {}
        for n in my_list:
            if n not in list_dict:
                list_dict[n]=0
            list_dict[n]+=1
        most_common =0
        for key,value in list_dict.items():
            if most_common<value:
                most_common=value
                most_appeared_num=key
        
        return most_appeared_num
    @classmethod
    def doubles(cls, my_list : list):
        list_dict= {}
        for n in my_list:
            if n not in list_dict:
                list_dict[n]=0
            list_dict[n]+=1

        num_of_unique_items=0
        for key,value in list_dict.items():
            if value >= 2:
                num_of_unique_items+=1

        return num_of_unique_items


if __name__=="__main__":
    numbers =[1, 5, 4, 5, 6, 7, 7, 5, 7, 7, 7]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))  