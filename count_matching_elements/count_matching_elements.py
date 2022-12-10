def count_matching_elements(my_matrix: list, element: int):
    count = 0
    i = 0
    j=0
    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            if my_matrix[i][j] != element:
                continue
            else :
                count+=1
    return count

if __name__=="__main__":
    m = [[1, 2, 3], [2, 3, 1], [4, 5, 6]]
    count = count_matching_elements(m, 2)
    print(count) #3