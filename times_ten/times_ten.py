def times_ten(start_index: int, end_index: int):
    d = {}
    value = []
    key = []
    i=j=start_index
    for i in range(start_index, end_index+1):
        value.append(i*10)
    
    for j in range(start_index, end_index+1):
        key.append(j)
    for index in range(len(key)):
        d[key[index]] = value[index]
    return d

if __name__=="__main__":
    d = times_ten(3, 6)
    print(d)