attempts = 0

while True :
    text = input("PIN: ")
    attempts += 1
    if text == "4321":
        break
    else:
        print("Wrong")

if attempts == 1 :
    print("Correct! It only took you one single attempt!")
else:
    print("Correct! It took you",attempts,"attempts")