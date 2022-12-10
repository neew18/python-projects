class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.inivalue = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value <= 0 :
            self.value = self.value
        else:  
            self.value -=1
        return self.value

    def set_to_zero(self):
        self.value= 0
        return self.value
    
    def reset_original_value(self) :
        self.value = self.inivalue
        return self.value



if __name__=="__main__":
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()