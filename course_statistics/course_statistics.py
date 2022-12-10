import urllib.request 
import json

def retrieve_all():
    address="https://studies.cs.helsinki.fi/stats-mock/api/courses"
    my_request= urllib.request.urlopen(address)
    my_request=my_request.read()
    json_=json.loads(my_request)
    active_courses_list=[]
    active_courses=()
    for course in json_:
        if course["enabled"] == True :
            active_courses = course["fullName"], course["name"], course["year"], sum(course["exercises"])
            active_courses_list.append(active_courses)
    return active_courses_list

def retrieve_course(course_name: str):
    address = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request= urllib.request.urlopen(address)
    my_request=my_request.read()
    json_=json.loads(my_request)

    weeks=[]
    for key in json_.items():
        weeks.append(key)

    hour_total =0
    exercise_total=0
    students=[]
    for key,value in json_.items():
        for x,y in value.items():
            if x == "hour_total":
                hour_total+= y
            if x == "exercise_total":
                exercise_total+= y
            amount_student = 0
            if x== 'students':
                students.append(y)
    
    
    average_hour= hour_total//students[0]

    average_exercise= exercise_total//students[0]

    retrieve_course_dict={}
    retrieve_course_dict['weeks']   = len(weeks)
    retrieve_course_dict['students'] = students[0]
    retrieve_course_dict['hours']    = hour_total
    retrieve_course_dict['hours_average'] = average_hour
    retrieve_course_dict['exercises']= exercise_total
    retrieve_course_dict['exercises_average']= average_exercise
    
    return retrieve_course_dict
    




if __name__=="__main__":
    print(retrieve_course("docker2019"))