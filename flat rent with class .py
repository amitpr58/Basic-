class Flat:
    def __init__(self , size , bathroom , rent , location):
        self.size=size
        self.bathroom=bathroom
        self.rent=rent
        self.location=location
    
    def increment_rate(self , increment_value):
        self.rent = self.rent + increment_value

    def change_location(self , new_location):
        self.location = new_location

    def decrement_rate(self,decrement_rate):
        self.rent=self.rent-decrement_rate

    def percentage_increment_rete(self,p):
        a=self.rent*p/100
        self.rent=self.rent+a



    def displayFlat(self):
        print(f"Size : {self.size} , bathromm : {self.bathroom} , rent : {self.rent} , location : {self.location}")

f1 = Flat("2bhk",1,2000 , "GN")
f1.displayFlat()

f1.increment_rate(1500)
f1.displayFlat()

f1.change_location("NOIDA")
f1.displayFlat()

f1.decrement_rate(150)
f1.displayFlat()

f1.percentage_increment_rete(15)
f1.displayFlat()
