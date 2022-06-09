# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according 
# to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, 
# condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the 
  # podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, 
# but also contains a special method called boost that will multiply 
# max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2

  def repair(self):
    self.condition = "NewCondition"
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update
# the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)

  def set_max_speed(self, newSpeed):
    self.max_speed(newSpeed)
  
  def flame_jet(self,other):
    other.condition = "trashed"

s = SebulbasPod(10,"perfect", 100)

s.max_speed = 500
s.set_max_speed(500)

'''
Make sure to answer the following prompts about your coding experience:
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
(1) Inheritance (2) encapsulation (3) polymorphism (4) abstraction

Abstraction is one of the most important features of object-oriented programming.
 It is used to hide the background details or any unnecessary implementation. Pre-defined functions are similar to data abstraction.
 abstraction is when all the unnecessary information is kept hidden from the users. 
 So we have here in our solution the abstraction in each class we created.

 Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
 It describes the idea of wrapping data and the methods that work on data within one unit. 
 This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
 To prevent accidental change, an object’s variable can only be changed by an object’s method. 
 Those types of variables are known as private variables. A class is an example of encapsulation as it encapsulates all the data 
 that is member functions, variables, etc.

 Polymorphism means the same function name (but different signatures) being used for different types.
 In our solution we see that in lines 15-16 and 28-29

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
How in particular did Object Oriented Programming assist in the solving of this problem?
'''