# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 17:39:47 2020

@author: vivek
"""

# object oriented programming
# we use class to define a user defined object
# from classes we can create an instance of the object
# an instance is a specific object created from a particular class

class NameOfClass(): # we are using camel casing, not snake casing like in functions
    def __init__(self,param1=default_value1,param2=default_value2): # we can pass default values for arguments (param1 is the argument)
        #self keyword is a reference to this particular instance of a class
        self.param=param1 # param is the attribute; attribute and argument names dont need to be same but by convention they are 
        self.param2=param2
        
    def some_mehod(self): 
        # perform some action
        print(self.param1)
        

        
class Dog():
    # class object attribute - these are the same for any instance of a class
    species='mammal'
    
    def __init__(self, breed1, height=40, weight=40, age=5, spots=False):
        self.breed=breed1 # convention is to just use breed in the three places, however we can use a different name (breed1 in this case) while we take in the argument
        self.height=height # here we follow the converntion and use height in all theee places (the name of the attribute (on the left), where we take in the argument (on the top), while assigning the argument (on the right) to the attribure 
        self.weight=weight
        self.age=age
        
        # we expect spots to be a boolean
        self.spots=spots

    # methods
    def bark(self):
        print('WOOF! my breed is {} and my species is {}'.format(self.breed, Dog.species)) # classes object attributes are referenced using class_name.attribute_name convention
        print(f'\nWOOF! my breed is {self.breed}')

#these are two specific instances of the Dog() class that we are defining
my_dog=Dog('poodle',45,15,4, False)        
my_dog2=Dog(breed1='lab',height=45,weight=15,age=4, spots=False)        

# attributes dont have () when we call them
print(my_dog.age)
print(my_dog.species) #class object attribute is same for all instances of a class

# methods have () when we call them
my_dog.bark()
my_dog2.bark()


# inheritence and polymorphish

# inheritence is a way to form new classes using classes that have been already defined

# example base class
class Animal():
    def __init__(self):
        print("animal created")
        
    def who_am_i(self):
        print('i am an animal')
        
    def eat(self):
        print('i am eating')
        
my_animal=Animal()

# lets recreate dog class 
# since we will be using some features from animal class, we can say that we will derive the Dog class from Animal class

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('dog created')
        
    def eat(self):
        print('i am a dog and i am eating') # you can overwite methods from base class or you can create new methods

        
my_dog3=Dog()

my_dog3.eat()




# polymorphism
# refers to the way in which different object classes can share the same method name
# those methods can be called from the same place even though a variety of different objects might be passed in

class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + ' says woof!!'

class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + ' says meow!!'

niko=Dog('niko')
felix=Cat('felix')

niko.speak()
felix.speak()

# example of polymorphism
# using for loop
for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

'''
<class '__main__.Dog'>
niko says woof!!
<class '__main__.Cat'>
felix says meow!!
'''

# example of polymorphism
# using def
def pet_speak(pet):
    print(pet.speak()) #since both classes use the method name speak

pet_speak(niko)
pet_speak(felix)




# abstract classes - these are never expected to be instantiated
# they are always expected to serve as a base class

class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError('subclass must implement this abstract method')
        
myanimal=Animal('tiger')
myanimal.speak()
#we will get an error saying that 'subclass must implement this abstract method'

#so we need to do the following

class Dog(Animal):
    def speak(self):
        return self.name + ' says woof!!'

class Cat(Animal):
    def speak(self):
        return self.name + ' says meow!!'

fido=Dog('fido')
isis=Cat('isis')

fido.speak()
isis.speak()


# special function - allow to use built in operations such as length or print with user objects
# these are also called magic or dunder methods
class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self): # this returns a string for print function to work for the object. we need a sring because print function expects a string that it can show as otput
        return f'{self.title} by {self.author}'
    # if we dont define the __str__ method then we will just get the location of the object when we try to print it
    def __len__(self):
        return self.pages
    def __del__(self):
        print('a book object was deleted')
        
b=Book('game of thrones','grr martin',5000)

print(b)
'''
game of thrones by grr martin
'''

len(b)
'''
Out[52]: 5000
'''

del b # can be used to delete the object
del(b) # this time along with deleting, python shows the message we defined in __del__ in the class


