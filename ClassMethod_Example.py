class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.age)
    
    def ageCalculation(self, name, year):
        self.year=2022-year
        self.name=name
        print('My name is ' + self.name + '. I am '+ str(self.year) + ' yeras old')

    @classmethod
    def ageCalculation1(cls, name, year):
        return cls(name, year)
    
    @staticmethod
    def ageCalculation2(age):
        if age>20:
            print(True)
        else:
            print(False)


person1=person('Sami', 32)
person1.ageCalculation('Samiul',1992)
person1.ageCalculation2(20)

person2=person.ageCalculation1('Emu', 2000)
print(person2.name)