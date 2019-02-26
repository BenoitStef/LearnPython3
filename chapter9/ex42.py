#-------------------------------------------------------------------------------
# is-a & has-a - Learn Python 3 the hard way - page 193
# Author    : Benoit Stef
# Date      : 26.02.2019
#-------------------------------------------------------------------------------
## Animal is-a object (yes, sort of confusion) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ##Dog has-a name
        self.name = name

##Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ##Cat has-a nam
        self.name = name

##Person is-a object
class Person(object):

    def __init__(self, name):
        ##Person has-a name
        self.name = name
        ##Person has-a pet of ome kind
        self.pet = None

##Emplyoee is-a Person
class Employee(Person)

    def __init__(self, name, salary):
    ##?? hmm what is this trange magic
        super(Employee, self).__init__(name)
        ##Emplyoee has-a salary
        self.salary = salary

##Fish is-a Object
class Fish(Object):
    pass

##Salmon is-a fish
class Salmon(Fish):
    pass

##Halibut is-a fish
class Halibut(Fish):
    pass

##satan is-a cat
satan = cat("Satan")

##Mary is-a Person
mary = Person("Mary")

##Mary has-a pet and his pet has-a name this pet is-a Animal
mary.pet = satan
##Franck is-a Employee and has-a name and has-a salary
franck = Employee("Frank",120000)
