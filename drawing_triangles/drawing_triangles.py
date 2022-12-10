def line(times, text):
    if text == "" :
        print("*"*times)
    else : 
        print(text*times)
def triangle(size):
    count = 1 
    times = 1
    while True :
        line(times,"#")
        if times == size :
            break
        count += 1
        times += 1
if __name__ == "__main__":
    triangle(5)