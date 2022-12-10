def filter_incorrect():
    import string
    correct=[] #to store the correct lottery numbers
    with open("lottery_numbers.csv") as file:
        for line in file :
            line1 = line
            line = line.replace("\n","")
            line = line.split(";")
            week = line[0].split(" ")
            nums = line[1].split(",")
            check=0
            error=0

            if week[1].isnumeric()==True: #check if the week number is incorrect
                check+=1
            if len(nums)==7: #check if there are seven the lottery numbers 
                check+=1
            for i in nums:
                if i.isnumeric()==True : #check if one or more numbers are not correct
                    if nums.count(i) == 1: #check if the same number appears twice
                        if 1<= int(i) <=39: #check if the numbers are too small or large
                            continue
                        else: 
                            error+=1
                    else: 
                        error+=1
                else: 
                    error+=1
            if error==0:
                check+=1  
        
            if check== 3:
                correct.append(line1)


    with open("correct_numbers.csv", "w") as correct_file :
        for a in correct:
            correct_file.write(a)
            
if __name__=="__main__":
    filter_incorrect()                
