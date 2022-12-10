def add_student(data: dict, name: str):
    data[name] = {}
        
def print_student(data: dict, name: str):  
    if name in data and len(data[name]) == 0:
        print(f"{name}:")
        print(" no completed courses")
        
    elif name in data:
        print(f"{name}:")
        print(f" {len(data[name])} completed courses:")
        for key, value in data[name].items():
            
            print(f"  {key}",end=" ")
            print(f"{value}")
            
        sum=0        
        for key,value in data[name].items():
            sum+=value
        
        length = len(data[name])
        mean = sum / length
        print(" average grade",mean )
              
    else : 
        print(f"{name}: no such person in the database")
        


def add_course(data: dict, name: str,course: tuple):
    if course[0] in data[name]:
        for key,value in data[name].items():
            if course[0] == key:
                if value<course[1]:
                    data[name][key]=course[1]
    else:
        if course[1] != 0:
            data[name][course[0]]=course[1]

def summary(data: dict):  
    print("students",len(data))

    course_complete={} #amount of completed courses of each student
    averages={} #average of grades of each student
    for key,value in data.items():
        course_complete[key]= len(value)
        sum=0
        for a,b in data[key].items():
            sum += b
            
        average= sum/len(value)
        averages[key]=average
    
    greatest=0
    for key,value in course_complete.items():
        if value>greatest:
            greatest=value
            person=key
    print(f"most courses completed {greatest} {person}") 
    
    greatest_average=0 
    for key,value in averages.items():
        if value>greatest_average:
            greatest_average=value
            person=key
    print(f"best average grade {greatest_average} {person}") 
        
if __name__=="__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)