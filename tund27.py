class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Display_Info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        
class Student(SchoolMember):
    def __init__(self, name, age, grade, subject):
        super().__init__(name, age)
        self.grade = grade
        self.subject = subject
        
    def Display_Info(self):
        super().Display_Info()
        print("Grades: ", self.grade)
        print("Subject: ", self.subject)
            
            
class Teacher(SchoolMember):
    def __init__(self, name, age, subject, years_of_experience):
        super().__init__(name, age)
        self.subject = subject
        self.years_of_experience = years_of_experience
        
    def Display_Info(self):
        super().Display_Info()
        print("Subject: ", self.subject)
        print("Years of Experience: ", self.years_of_experience)
            
class Staff(SchoolMember):
    def __init__(self, name, age, position, department):
        super().__init__(name, age)
        self.position = position
        self.department = department
        
    def Display_Info(self):
        super().Display_Info()
        print("Position: ", self.position)
        print("Department: ", self.department)
            
class School:
    def __init__(self):
        self.members = []
        
    def Display_all_members(self):
        print("All members:")
        for member in self.members:
            member.Display_Info()
            print("--------------------------------")
            
    def Add_Member(self, member):
        self.members.append(member)
        
    def remove_member(self,name):
        too_delete = None
        for member in self.members:
            if member.name == name:
                too_delete = member
                self.members.remove(member)


Cleaner = Staff("Piter",23,"Cleaner","service")
SiSAdmin = Staff("Pedro",69,"SiSAdmin","service")
#Cleaner.Display_Info()
School1 = School()
School1.Add_Member(Cleaner)
School1.Add_Member(SiSAdmin)
School1.Display_all_members()


School1.remove_member("Piter")
print("zabanen")
School1.Display_all_members()