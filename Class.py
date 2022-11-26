class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self, newName):
    self.newName=newName
    print("Hello, my name is " + self.newName)

p1 = Person("John", 36)
p1.myfunc('Samiul')