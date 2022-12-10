class Course:
    def __init__(self,name:str) :
        self.__course_name=name
        self._grade=0
        self._credits=0
    
    def name(self):
        return self.__course_name
    
    def grade(self):
        return self._grade
    
    def credits(self):
        return self._credits

    def add_data(self,grade:int,credits:int):
        if grade > self._grade:
            self._grade=grade
        if credits> self._credits:
            self._credits=credits

class Courses:
    def __init__(self) :
        self._courses={}
    
    def add_data(self,name:str,grade:int,credits:int):
        c=Course(name)
        if name not in self._courses:
            self._courses[name]=c

        self._courses[name].add_data(grade,credits)

    def get_course(self,name:str):
        if name not in self._courses:
            return None
        return self._courses[name]._credits,self._courses[name]._grade

    def get_all_courses(self):
        return self._courses

class Courses_Application:
    def __init__(self):
        self._courses=Courses()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course_name=input("course: ")
        grade=int(input("grade: "))
        credits=int(input("credits: "))

        self._courses.add_data(course_name,grade,credits)


    def get_course_data(self):
        course_name=input("course: ")

        if self._courses.get_course(course_name) == None:
            print("no entry for this course")
        else:
            print(f"{course_name} ({self._courses.get_course(course_name)[0]} cr) grade {self._courses.get_course(course_name)[1]}")
    def statistics(self):
        total_courses=0
        total_credits=0
        total_grades_list=[]
        for k,v in self._courses.get_all_courses().items():
            total_courses+=1
            total_credits+= v._credits
            total_grades_list.append(v._grade)

        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {sum(total_grades_list)/total_courses:.1f}")
        print("grade distribution")
        grade = 5
        while grade>=0:
            number_of_grades = total_grades_list.count(grade)*"x"
            print(f"{grade}: {number_of_grades}")
            grade-=1

    def execute(self):
        self.help()

        while True:
            print("")
            command=input("command: ")

            if command=="1":
                self.add_course()
            
            elif command=="2":
                self.get_course_data()

            elif command=="3":
                self.statistics()

            elif command=="0":
                break

e=Courses_Application()
e.execute()