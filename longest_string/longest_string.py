def longest(strings: list):
    result = max(strings, key=len)
    return result
    
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))