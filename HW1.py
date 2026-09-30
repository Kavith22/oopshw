class student():
    def __init__(self,name,grade,school_name):
        self.school_name=school_name
        self.name=name
        self.grade=grade
    def show_details(self):
        print(self.name)
        print(self.grade)
        print(self.school_name)
c=student('sam',9,'School')

c.show_details()