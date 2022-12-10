def smallest_average(person1: dict, person2: dict, person3: dict):
    averages={}
    
    person1_sum= person1["result1"] + person1["result2"]+ person1["result3"]
    person1_average= person1_sum/ 3 
    averages["person1"]= person1_average
       
    person2_sum= person2["result1"] + person2["result2"]+ person2["result3"]
    person2_average= person2_sum/ 3 
    averages["person2"]= person2_average
   
    person3_sum= person3["result1"] + person3["result2"]+ person3["result3"]
    person3_average= person3_sum/ 3 
    averages['person3']= person3_average
    
    average_list=[]
    for key,value in averages.items():
        average_list.append(value)
    smallest= min(average_list)
    
    for key,value in averages.items():
        if smallest == value:
            person = key
    

    if person == "person1":
        result= person1
    elif person == "person2":
        result = person2
    elif person == "person3":
        result = person3
    return result
    
if __name__=="__main__":
    person1 = {"name": "Anna", "result1": 1,"result2": 1,"result3": 1}
    person2 = {"name": "Anna", "result1": 2,"result2": 2,"result3": 2}
    person3 = {"name": "Anna", "result1": 3,"result2": 3,"result3": 3}

    print(smallest_average(person1, person2, person3))