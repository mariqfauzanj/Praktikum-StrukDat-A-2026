class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

# Create the Animal class

class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(f"Hi!")

# Create the Dog class (inherits from Animal)
class Dog(Animal):
  pass

# Create an object

d1 = Dog("Rex")
# Call the speak method
d1.speak()