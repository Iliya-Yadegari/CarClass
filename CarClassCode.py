class Car:
    def __init__(self,name,plateNum,yearMade):
        self.name = name
        self.plateNum = plateNum
        self.yearMade = yearMade
        
    def objectPrint(self):
        
        print(f'The name of this car is {self.name}, the plate number is {self.plateNum} and the year made is {self.yearMade}')
        
    def checkAge(self):
        
        age = 2021 - self.yearMade
        
        if age > 20:
            print('TOO OLD PLEASE MAKE SURE OF THE SAFETIES')
            
bmw = Car('BMW','K235KS7',2004)

bmw.checkAge()
bmw.objectPrint()