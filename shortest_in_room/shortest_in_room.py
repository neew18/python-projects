class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
class Room:
    def __init__(self):
        self.persons=[]
        self.heights=[]

    def add(self,person: Person):
        self.persons.append(person)
        self.heights.append(person.height)
    
    def is_empty(self):
        if len(self.persons) == 0 :
            return True
        else:
            return False

    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum(self.heights)} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self) :
        if len(self.persons) == 0 :
            return None
        else:   
            shortest= min(self.heights)
            for person in self.persons:
                if person.height==shortest:
                    return person

    def remove_shortest(self):
        if len(self.persons) == 0 :
            return None
        else:   
            shortest= self.shortest()
            self.persons.remove(shortest)
            self.heights.remove(shortest.height)
            return shortest
        
                    

            
            
if __name__=="__main__":
    room = Room()

    room.add(Person("Ann",120))
    room.add(Person("Tim",150))
   
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {id(removed)}")

    print()

    room.print_contents()