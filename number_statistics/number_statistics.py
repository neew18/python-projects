class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum=0
        self.even=0
        self.odd=0
    
    def add_number(self, number:input):
        self.numbers+=1
        self.sum+=number
        pass
    def add_even(self,number:input):
        if number%2==0:
            self.even+=number
        return self.even
    def add_odd(self,number:input):
        if number%2!=0:
            self.odd+=number
        return self.odd
    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        try: 
            self.numbers>0
            return self.sum
        except:
            return 0
        
    def average(self):
        try:
            self.numbers > 0 
            return self.sum/self.numbers
        except:
            return 0


stats = NumberStats()
print("Please type in integer numbers:")
while True:
    number= int(input(""))
    if number==-1:
        break
    if number%2==0:
        stats.add_even(number)
    else :
        stats.add_odd(number)
    stats.add_number(number)
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", stats.even)
print("Sum of odd numbers:", stats.odd)