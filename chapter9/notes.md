### Object Oriented Programming Basics

-  Classes are like blueprints or definitions for creating new mini-modules.  

-  Instantiation is how you make one of these mini-modules and import it at the same time. ”Instantiate”
just means to create an object from the class.  

-   The resulting created mini-module is called an object, and you then assign it to a variable to work
with it.

##### dict style
mystuff['apples']

##### module style
mystuff.apples()
print(mystuff.tangerine)

##### class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)

***
Why do I need self when I make "init" or other functions for classes? If you don’t have self, then code like cheese = 'Frank' is ambiguous. That code isn’t clear about whether you mean the instance’s cheese attribute or a local variable named cheese. With self.cheese = 'Frank' it’s very clear you mean the instance attribute self.cheese.
***

**class** Tell Python to make a new type of thing.

**object** Two meanings: the most basic type of thing, and any instance of some thing.

**instance** What you get when you tell Python to create a class.

**def** How you define a function inside a class.

**self** Inside the functions in a class, self is a variable for the instance/object being accessed.

**inheritance** The concept that one class can inherit traits from another class, much like you and your parents.

**composition** The concept that a class can be composed of other classes as parts, much like how a car has wheels.

**attribute** A property classes have that are from composition and are usually variables.

**is-a** A phrase to say that something inherits from another, as in a ”salmon” is-a ”fish.”

**has-a** A phrase to say that something is composed of other things or has a trait, as in ”a salmon has-a mouth.”
