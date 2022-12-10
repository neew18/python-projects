def palindromes(word: str):
    backward = word[::-1]
    if word == backward:
        return True
    else:
        return False

def main():  
    while True:
        text = input("Please type in a palindrome: ")
        backward = palindromes(text)
        if backward== True:
            print(f"{text} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")
            
main()