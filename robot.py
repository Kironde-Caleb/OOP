##Abstract 

class Robot:
    def make_popcorn(self):
        self._heat_pan()
        self._add_oil()
        self._pop_the_corn()
        print("Popcorn is ready")
        
    def _heat_pan(self):
        print("Heating the pan")
    
    def _add_oil(self):
        print("Adding oil")
        
    def _pop_the_corn(self):
        print("Popping")



robot = Robot()

robot.make_popcorn()



