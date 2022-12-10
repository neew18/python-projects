def most_common_character(string):
    dict={}
    for character in string:
        dict[character] = string.count(character)
    
    return max(dict, key = dict.get)

if __name__=="__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string)) #b

    second_string = "exemplaryelementary"
    print(most_common_character(second_string)) #e