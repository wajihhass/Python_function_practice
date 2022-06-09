# Implement a function that will flatten and sort an array of integers 
# in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flatten_and_sort([[12,55,1],[2,33,4],[88,44,3,0]]))
print(flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]]))
print(flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]]))

'''
How does this solution ensure data immutability?

    Mutable Definition:
        Mutable is when something is changeable or has the ability to change. 
        So, the simplest definition is: An object whose internal state can be changed is mutable
        In Python, ‘mutable’ is the ability of objects to change their values. 
    
    These are often the objects that store a collection of data.

    List of Mutable  objects
        Objects of built-in type that are mutable are:
        Lists
        Sets
        Dictionaries

    Immutable Definition:
        Immutable is the when no change is possible over time.
        In Python, if the value of an object cannot be changed over time, then it is known as immutable.
        Once created, the value of these objects is permanent. So, immutable doesn’t allow any change in the object once it has been created.
    Objects of built-in type that are immutable are:

        Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
        Strings
        Tuples
        Frozen Sets

So the up codes are mutable so the solution is a list we can add any elements to the list as seen in the following output:
print(flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]]))
[1, 2, 3, 4, 12, 33, 44, 55, 88]
>>> print(flatten_and_sort([[12,55,1],[2,33,4],[88,44,3,0]]))
[0, 1, 2, 3, 4, 12, 33, 44, 55, 88].


Is this solution a pure function? Why or why not?
A pure function is a function that will return the same values given the same arguments. 
A function is not pure if there is something outside the function that can change its return, given the same arguments.
So the solution is a pure function because it will has the same output with the same arguments.
 There is no global variable that may be changed and so the output of this function will be changed for the same arguments.

Is this solution a higher order function? Why or why not?
Higher-order functions is one that does one or both of the following:
-Accepts one or more functions as an argument
-Returns a function.
So the solution is not a higher function.
Would it have been easier to solve this problem using a different programming style?
Yes
Why in particular is functional programming a helpful paradigm when solving this problem?
because the functional programming basicly use functions.
'''

class TestArray:
    def __init__(self):
        self.arr = []

    def flatten_and_sort(self, newArray):
        for item in newArray:
            for i in item:
                self.arr.append(i)
        return sorted(self.arr)

testOOP = TestArray()
testResult1 = testOOP.flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]])
testResult2 = testOOP.flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]])
testResult3 = testOOP.flatten_and_sort([[12,55,1],[2,33,4],[88,44,3]])
print(testResult1)
print(testResult2)
print(testResult3)