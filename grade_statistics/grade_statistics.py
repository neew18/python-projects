def input_user(): #(input: int)
    x = [] #exam points 0-20
    y = [] #exercise  completed 0-100
    while True :
        result = input("Exam points and exercises completed: ")
        if result == "":
            break
        splitted = result.split()
        
        x.append(int(splitted[0]))
        y.append(int(splitted[1]))
        tuple_input = x, y
    return tuple_input

def points(tuple_input: tuple):
    i = [] #converting the exercise points
    failed = []
    total_points= [] #total points (exams  + exercises)
    for exercise in tuple_input[1] :
        if 0 <= exercise <= 9 :
            exercise_points = 0 
        elif 10 <= exercise <= 19 :
            exercise_points = 1
        elif 20 <= exercise <= 29 :
            exercise_points = 2
        elif 30 <= exercise <= 39 :
            exercise_points = 3
        elif 40 <= exercise  <= 49 :
            exercise_points = 4
        elif 50 <= exercise  <= 59 :
            exercise_points = 5
        elif 60 <= exercise  <= 69 :
            exercise_points = 6
        elif 70 <= exercise  <= 79 :
            exercise_points = 7
        elif 80 <=exercise  <= 89 :
            exercise_points = 8
        elif 90 <= exercise <= 99 :
            exercise_points = 9
        elif  exercise  == 100 :
            exercise_points = 10
        
        i.append(exercise_points)
        
    #Calculating total points and converting them into grades
    for index in range(0,len(tuple_input[0])):
        total= tuple_input[0][index]+ i[index]
        total_points.append(total)
        if tuple_input[0][index] < 10:
            failed.append(0)
        else:
            failed.append(tuple_input[0][index])
    
    return total_points, failed
    
def grades(tl_points: list, failed: list):
    grades=[] #converting into grades
    for a in tl_points:
        if a <= 14:
            grade=0
        elif 15<= a <=17 :
            grade=1
        elif 18<= a <=20 :
            grade=2
        elif 21<= a <=23 :
            grade=3
        elif 24<= a<=27 :
            grade=4
        elif 28<= a <=30 :
            grade=5
        
        grades.append(grade)
    failed_grades=grades[:]
    for i in range(0,len(failed_grades))   :
        if failed[i] == 0:
            failed_grades[i]=0
    return grades, failed_grades
    
def statistics_average(grades: list):
    average= sum(grades)/len(grades)  
    return average
    
def statistics_percentage(b: list):
    pass_percentage= 100*(len(b) - b.count(0)) / len(b)  
    return pass_percentage
    
def main():
    input, failed = points(input_user())
    grades_list, failed_grades =  grades(input, failed)
    print("Statistics:")
    average = statistics_average(input)
    print(f"Points average: {average:.1f}")
    percentage = statistics_percentage(failed_grades)
    print(f"Pass percentage: {percentage:.1f}")
    print("Grade distribution:")
    grade = 5
    while grade>=0:
        number_of_grades = failed_grades.count(grade)*"*"
        print(f"  {grade}: {number_of_grades}")
        grade-=1

main()
        
       


