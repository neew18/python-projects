def  oldest_person(people: list):

    years = []
    for person in people:
        years.append(person[1])
        
    max_year= sorted(years)[0]
    
    for person in people:
        if max_year == person[1]:
            oldest = person[0]
            
    return oldest

if __name__=="__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))