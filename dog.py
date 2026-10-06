##COMPOSITION 

##Composiiton is a design principle where we make a complex class by combing simpler independet classes

class Tail:
    def wag(self):
        print("Wag wag")

class DOg:
    def __init__(self, name):
        self.name = name 
        self.tail = Tail()


    def greet(self):
        print("Woof woof, Happy to see you")
        self.tail.wag()


        