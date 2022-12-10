class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str,password:str):
        super().__init__(name)
        self.password=password
        self.dict={}

    def add_ingredient(self,ingredient: str, amount: float, password: str):
        super().add_ingredient(ingredient, amount)
        if password==self.password:
            self.dict[password]=self._ingredients
        else:
            raise ValueError ("Wrong password!")

    def print_recipe(self,password: str):
        
        if password in self.dict:
            print(self._name + ":")
            for key,value in self.dict.items():
            
                if key== self.password:
                    for i in value:
                        print(f"{i[0]} {i[1]} grams")
        else:
            raise ValueError ("Wrong password!")

if __name__=="__main__":
    diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
    diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
    diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
    diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
    diminuendo.print_recipe("hocuspocus")

    diminuendo.print_recipe("pocushocus") # WRONG password!