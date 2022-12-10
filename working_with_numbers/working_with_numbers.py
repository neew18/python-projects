print("Please type in integer numbers. Type in 0 to finish.")
attempt= 0
sum = 0
mean = 0
negative=0
positive=0
while True:
    number = int(input("Number:"))
    attempt += 1
    if number == 0 :
        break
    sum+= number
    mean = sum/attempt
    if number> 0:
        positive+=1
    if number < 0 and number != 0:
        negative+=1

print("... the program asks for numbers")
print("Numbers typed in",attempt-1)
print("The sum of the numbers is",sum)
print("The mean of the numbers is",mean)
print("Positive numbers",positive)
print("Negative numbers",negative)
    