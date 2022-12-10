print("What is the weather forecast for tomorrow?")

x = int(input("Temperature: ")) 
y = input("Will it rain (yes/no): ")

print("Wear jeans and a T-shirt")

if x <= 20  :
    print("I recommend a jumper as well")

if x <= 10 :
    print("Take a jacket with you")
    
if x <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
        
if y == "yes":    
    print("Don't forget your umbrella!")
else:
    print()