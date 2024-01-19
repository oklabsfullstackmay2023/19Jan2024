#1 class deifnation is one time process
class Bowler(): 
    #1. property/variable
    speed=""
    #2. constructor/esp.function
    def __init__(self,s):
        self.speed=s
        pass
    #3. function/method
    pass
class FastPacer(Bowler):
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self,s):
        super().__init__(s)
        pass
    #3. method/function
    pass
class MediumPacer(Bowler):
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self,s):
        super().__init__(s)
        pass
    #3. method/function
    pass
class Spinner(Bowler):
    #1. property/variable
    #2. constructor/esp.function
    def __init__(self,s):
        super().__init__(s)
        pass
    #3. method/function
    pass

#2. create class external object is many time process
jaspritbhumrah=FastPacer(153.45)
print(f'The Bowling speed of JaspritBumrah is {jaspritbhumrah.speed} kmph')
arshadeeepsingh=MediumPacer(130)
print(f'The Bowling Speed of ArshadeepSingh is {arshadeeepsingh.speed} kmph')
ravindrajadeja=Spinner(97)
print(f'The Bowling Speed of RavindraJadeja is {ravindrajadeja.speed} kmph')

