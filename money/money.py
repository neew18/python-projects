class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents < 10:
            return f"{self.__euros}.0{self.__cents} eur"

        else: 
            return f"{self.__euros}.{self.__cents} eur"
    def __eq__(self, another):
        if self.__euros==another.__euros and self.__cents==another.__cents:
            return True
        else:
            return False
    def __ne__(self, another):
        if self.__euros!=another.__euros :
            if self.__cents!=another.__cents:
                return True
            elif self.__cents==another.__cents:
                return True
            else:
                return False
        elif self.__euros==another.__euros :
            if self.__cents!=another.__cents:
                return True
            else:
                return False

    def __lt__(self,another):
        if self.__euros<another.__euros :
            if self.__cents<=another.__cents:
                return True
            else:
                return False
        elif self.__euros==another.__euros :
            if self.__cents<another.__cents:
                return True
            else:
                return False
        else:
            return False
    def __gt__(self,another):
        if self.__euros>another.__euros :
            if self.__cents>=another.__cents:
                return True
            else:
                return False
        elif self.__euros==another.__euros :
            if self.__cents>another.__cents:
                return True
            else:
                return False
        else:
            return False
    def __add__(self,another):
        addition_euros=self.__euros+another.__euros
        addition_cents=self.__cents+another.__cents
        if addition_cents>=100:
            addition_euros+=1
            addition_cents-=100
        if addition_cents == 0 :
            return f"{addition_euros}.00 eur"
        else:
            return f"{addition_euros}.{addition_cents} eur"

        

    def __sub__(self,another):
        sub_euros=self.__euros-another.__euros
        if self.__euros<another.__euros :
            raise ValueError(f"a negative result is not allowed")
        elif self.__euros==another.__euros :   
            if self.__cents<another.__cents:
                raise ValueError(f"a negative result is not allowed")
            elif self.__cents==another.__cents:
                return f"0.00 eur"
            else:
                sub_cents=self.__cents-another.__cents
                if sub_cents<10:
                    return f"{sub_euros}.0{sub_cents} eur"
                else:
                    return f"{sub_euros}.{sub_cents} eur"
        else:
            if self.__cents<another.__cents:
                sub_cents=(self.__cents+100)-another.__cents
                sub_euros-=1
                return f"{sub_euros}.{sub_cents} eur"
            else:
                sub_cents=self.__cents-another.__cents
                if sub_cents==0:
                    return f"{sub_euros}.00 eur"
                else:
                    return f"{sub_euros}.{sub_cents} eur"
        

if __name__=="__main__":
    money1 = Money(4, 95)
    money2 = Money(4, 90)
    e4 = money1 - money2
    print(e4)