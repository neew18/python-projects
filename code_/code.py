class Item:
    def __init__(self,name_:str,weight_:int):
        self.__name_=name_
        self.__weight_=weight_
    def __str__(self) :
        return f"{self.__name_} ({self.__weight_} kg)"
    def name(self):       
        return self.__name_
    
    def weight(self):
        return self.__weight_


class Suitcase:
    def __init__(self,max_weight:int) :
        self.max_weight=max_weight
        self.add_items=[]
        self.weights=0
        self.dict_items={}
    def add_item(self,item):
        x= self.weights+item.weight() 
        if x <= self.max_weight:
            self.weights+= item.weight()
            self.add_items.append(item) 
            self.dict_items[item.weight()]  = item 

    def __str__(self) :
        if len(self.add_items) == 1:
            return f"{len(self.add_items)} item ({self.weights} kg)"
        else:
            return f"{len(self.add_items)} items ({self.weights} kg)"
        
    def print_items(self):
        for i in self.add_items:
            print(i)      

    def weight(self):
        return self.weights 

    def heaviest_item(self):
        if len(self.add_items)==0:
            return None
        else:
            most=0
            for key,value in self.dict_items.items():
                if most<key:
                    most=key
                    result=value
            return result

class CargoHold:
    def __init__(self,max_weight:int):
        self.max_weight=max_weight
        self.num_of_suitcases=[]
        self.items_lists=[]

    def add_suitcase(self,suitcase):
        if self.max_weight>=suitcase.weight():
            self.max_weight-=suitcase.weight()
            self.num_of_suitcases.append(suitcase)
            
        for b in suitcase.add_items:
            self.items_lists.append(b)
    
    def __str__(self):
        if len(self.num_of_suitcases)==1:
            return f"{len(self.num_of_suitcases)} suitcase, space for {self.max_weight} kg"
        else:
            return f"{len(self.num_of_suitcases)} suitcases, space for {self.max_weight} kg"

    def print_items(self):
        for a in self.items_lists:
            print(a)

if __name__=="__main__":
    hold = CargoHold(10)
    suitcase = Suitcase(25)
    item = Item("Anvil", 24)
    suitcase.add_item(item)
    hold.add_suitcase(suitcase)
    print(hold)