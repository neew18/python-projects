#Generally, any year that is divisible by four is a leap year.
#However, if the year is additionally divisible by 100, 
#it is a leap year only if it also divisible by 400.

year = int(input("Type in a year: " ))

if year % 4 == 0 :
    if year % 100 ==0:
        if year % 400==0 :
            print("This year is a leap year")
        else: 
            print("This year is not a leap year")
    else:
        print("This year is a leap year")
else:
    print("This year is not a leap year")