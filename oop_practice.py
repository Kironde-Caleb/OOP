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


class Lead_actor(Actor):
    def __init__(self, role="lead actor", script="recieved script", salary = "$300"):
        super().__init__()
        self.role = role
        self.script = script
        self.__salary = salary

    def get_salary(self):
        print(self.__salary, "per hour")
    

    def project_details(self):
        print(self.name, self.role, ":", self.script)
        self.get_salary()

class Support_actor(Actor):
    def __init__(self, role="support actor", script="recieved script", salary = "$150"):
        super().__init__()
        self.role = role
        self.script = script

    def get_salary(self):
            print(self.__salary, "per hour")
    
    def project_details(self):
        print(self.name, self.role, ":", self.script, "in bits")
        self.get_salary()

class Extra_actor(Actor):
    def __init__(self, role="extra actor", script="no script", salary = "$50"):
        super().__init__()
        self.role = role
        self.script = script

    def get_salary(self):
            print(self.__salary, "per hour")

    def project_details(self):
        print(self.name, self.role, ":", self.script, "just director's directions")
        self.get_salary()

        
        
actor1 = Lead_actor()
actor2 = Lead_actor()
actor3 = Lead_actor()

for x in (actor1, actor2, actor3):
    x.project_details()
