class Clock:
    def __init__(self,hours,minutes,seconds):
        self.hours=hours
        self.seconds = seconds
        self.minutes = minutes

    def tick(self):
        if self.seconds <= 59: #seconds under 59
            self.seconds+=1
        if self.seconds >= 60: #seconds over 60
            self.seconds=0
            self.minutes+=1
        if self.minutes >= 60: #minutes 0ver 60 
            self.minutes=0
            self.hours+=1
        if self.hours >= 24:
            self.hours =0
        
    def set(self,hours,minutes):
        self.hours= hours
        self.minutes=minutes
        self.seconds=0
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


if __name__=="__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)