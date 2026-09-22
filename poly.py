class PhoneAlarm:
    def__init__(self, snooze_count = 0):
        self.snooze_count = snooze_count
        
    def wake_me_up(self):
        return "Scream at full volume"

class Roomate:
    def__init__(self, name):
        self.name = name 
    
    def wake_me_up(self):
        return f"{self.name} pours water on you"

class MotherCall:
    def wake_me_up(self):
        return "Calls at 4:30am"

class SunlightThroughTheWindow:
    def__init__(self):
        return "Sunlight creeps in"

morning = [PhoneAlarm(5), Roomate("OC"), MotherCall(), SunlightThroughTheWindow()]    


def start_your_day(wake_up_method):
    return wake_up_method.wake_me_up()

for tap_me in morning:
    print(start_your_day(tap_me))
