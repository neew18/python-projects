from functools import reduce
class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(my_list:list):
    return reduce(lambda reduced_sum,item:reduced_sum+item.credits,my_list,0)

def sum_of_passed_credits(my_list:list):
    passed=list(filter(lambda item: item.grade>=1,my_list))
    return reduce(lambda reduced_sum,item: reduced_sum+item.credits,passed,0)

def average(my_list:list):
    passed=list(filter(lambda item: item.grade>=1,my_list))
    passed_sum=reduce(lambda reduced_sum,item: reduced_sum+item.grade,passed,0)
    mean=passed_sum/len(passed)
    return mean
if __name__=="__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)   