#class 
class Student:
    '''A student class'''
    stuCount= 0
    def __init__(self , name , rollno , branch , semester):
        self.name = name
        self.rollno = rollno
        self.branch= branch
        self.semester=semester
        Student.stuCount += 1

#function update 
    def update_name(self ,name):
        self.name = name
    def update_rollno(self ,rollno):
        self.rollno = rollno
    def update_branch(self, branch):
        self.branch= branch 
    def update_semester(self,semester):
        self.semester=semester
        
    def update_details(self , **data):
        print(data)
        if 'name' in data:
            self.name = data['name']
        if 'rollno' in data:
            self.rollno = data['rollno']
        if 'branch'in  data:
            self.branch=data['branch']
        if 'semester' in data :
            self.semester=data['semester']
            

    def displayStudent(self):
        print("Name:",self.name,"Rollno:",self.rollno,"Branch:",self.branch,"semester:",self.semester)
        


stu1 = Student("Amit" , 101 , "ECE" , 6)
stu2 = Student("VED" , 102 , "IT" , 8)
stu1.displayStudent()
stu2.displayStudent()

stu1.update_details(name="VED" , rollno=102)
stu1.displayStudent()


stu2.update_details(semester=90003,branch="ece")
stu2.displayStudent()
