#a class is like a blue print for creating objects. an object has properties and methods (functions) associated with it. Almost everything in prthon is an object

#create class 
class User:
#constructor
  def _init_(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

    def greeting(self):
      return f'my name is {self.name} and i am {self.age}'

#init user object
john = User('John ezeokafor', 'johnzkfr@gmail.com', 17)
print(john.greeting())
 