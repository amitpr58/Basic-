class Sunglass:
    def __init__(self , powerLence , normalLence , hybridLence):
        self.powerLence=powerLence
        self.normalLence=normalLence
        self.hybridLence=hybridLence

    def percentageIncreaseRate(self , p):
        inhence=self.powerLence*p/100
        self.powerLence =self.powerLence+inhence

    def percentageIncreaseRate(self,p):
        inhence=self.normalLence*p/100
        self.normalLence=self.normalLence+inhence



    def displaySunglass(self):
        print("\npowerLence = ", self.powerLence,"\nnormalLence:", self.normalLence,"\nhybridLence:",self.hybridLence)


glass=Sunglass(500,750,1000)
#print()
glass.displaySunglass()
glass.percentageIncreaseRate(10)
glass.displaySunglass()
