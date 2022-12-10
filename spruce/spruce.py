def spruce(size):
    print("a spruce!")  
    character = "*"
    stemsize = size
    stemcharacter = character
    while size > 0:
        Spruce = " "*(size-1)+character
        print(Spruce)
        character+="**"
        size -=1
    newsize = size//2
    print (" " * (stemsize-1) + stemcharacter)    
    
        
if __name__ == "__main__":
    spruce(5)