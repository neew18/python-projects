def double_items(numbers: list):
    numbers_doubled=[]
    for item in numbers :
        numbers_doubled.append(item*2)
    return numbers_doubled
        
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)         #original: [2, 4, 5, 3, 11, -4]
    print("doubled:", numbers_doubled)  #doubled: [4, 8, 10, 6, 22, -8]