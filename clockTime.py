class clockTime:

    #Constructor
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    
    #Set hours 
    def setHours(self,hours):
        self.hours = hours

    #Set mins
    def setMinutes(self,minutes):
        self.minutes = minutes

    #Set seconds
    def setSeconds(self, seconds):
        self.seconds = seconds

    #Set Time
    def setTime(self,hours,minutes,seconds):
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)

    #Display time
    def showTime(self):
        print("Time: " + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))


time = clockTime()
hours = int(input("Enter hours value: "))
minutes = int(input("Enter minutes value: "))
seconds = int(input("Enter seconds value: "))
time.setTime(hours,minutes,seconds)
time.showTime()


        