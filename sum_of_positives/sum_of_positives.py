def sum_of_positives(my_list):
    sum = 0 
    for i in my_list:
       if i > 0:
           sum = sum + i
    result = sum
    return result

if __name__=="__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)