class LotteryNumbers:
    def __init__(self,week_num:int,list_int: list) :
        self._week_num=week_num
        self._list_int=list_int

    def number_of_hits(self,numbers: list):
        return  len([ x for x in numbers if x in self._list_int])

    def hits_in_place(self,numbers):
        return [i if i in self._list_int else -1 for i in numbers]
if __name__=="__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))