#define class name=company,
#create company name =talkmore
#total member,salary
class company:
    '''A company class'''
    
    def __init__  (self, companyname ,empoly,maximumsalary,minimumsalary , skills):
        self.companyname= companyname
        self.empoly=empoly
        self.maximumsalary=maximumsalary
        self.minimumsalary=minimumsalary
        self.skills = skills

    def addSkill(self ,skill):
        """self.skills : list[string] +skills"""
        self.skills.append(skill)

    def showAllSkills(self):
        print(self.skills)


    def displayCompany(self):
        print("Talkmore:", "empoly:",self.empoly,"maximum salary:",self.maximumsalary,"minimum salary:",self.minimumsalary )



talkmore=company("talkmore",256,500000,20000 , ["Python" , "java","c"])
talkmore.displayCompany()
talkmore.showAllSkills()

talkmore.addSkill("c++")
talkmore.showAllSkills()
