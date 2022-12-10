class SimpleDate:
    def __init__(self,day:int, month:int, year:int):
        self.day=day
        self.month=month
        self.year=year
    def __str__(self) :
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self,another):
        if self.year==another.year and self.month==another.month and self.day==another.day:
            return True
        else:
            return False
    def __ne__(self, another) :
        if self.year!=another.year or self.month!=another.month or self.day!=another.day:
            return True
        else:
            return False

    def __gt__(self,another):
        if self.year>=another.year:
            if self.month>=another.month:
                if self.day>=another.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __lt__(self,another):
        if self.year<=another.year:
            if self.month<=another.month:
                if self.day<=another.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __add__(self,amount:int):
        days=self.day+amount
        months=self.month
        years=self.year
        if days>30:
            months+=days//30
            days=days%30
        if months>12:
            years+=months//12
            months=months%12
        
        return SimpleDate(days,months,years)

    def __sub__(self,another):
        days=self.day-another.day
        months=self.month-another.month
        years=self.year-another.year
       
        if years>0:
            months+=years*12
        elif years<0:
            months+=years*12
        if months>0:
            days+=months*30
        elif months<0:
            days+=months*30
            days=-days
        return days
if __name__=="__main__":
    sd1 = SimpleDate(1, 1, 1900)
    sd2 = SimpleDate(1, 1, 1901)

    print(sd1 < sd2)