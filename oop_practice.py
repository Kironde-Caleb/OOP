print(50*"=")
print("ACTORS REGISTRATION SHEET🎭")
print(50*"=")
print()

class Person:
    def __init__(self):

        name = input("insert name: ")
        age = int(input("insert age: "))
        gender = input("insert your gender: ")
        address = input("insert your address: ")
        contact = input("insert your conatact: ")

        self.name = name
        self.age = age
        self.gender = gender 
        self.address = address
        self.contact = contact 


    def introduce(self):
        print()
        print("ACTOR BIO")
        print(50*"=")
        print("name :", self.name)
        print("age :", self.age)
        print("gender :", self.gender)
        print("address :", self.address)
        print("contact :", self.contact)

class Actor(Person):
    def __init__(self):
        super().__init__()

        currentShow = input("insert your current show: ")
        credits = input("insert your credits(ë.g.Role/Show/Where): ")
        education = input("insert your education: ")
        print()
         
        self.currentShow = currentShow
        self.credits = credits
        self.education = education 

        

    def introduce(self):
        super().introduce()
        print("current show :", self.currentShow)
        print("credit:", self.credits)
        print("education :", self.education)
        
        
actor1 = Actor()
actor2 = Actor()

actor1.introduce()
actor2.introduce()