# -*- coding: utf-8 -*-
# Operations on tuples
t1 = (1, 'two', 3)
t2 = (t1, 'four')
print t1 + t2 # concatenation
print (t1 + t2)[3] # Indexing
print (t1 + t2)[2:5] # Slicing
t3 = ('five',) # Singletons

# Manipulating tuples
# Can iterate over tuples just as we can iterate over strings
def findDivisors(n1, n2):
    """assume n1 and n2 positive ints returns tuple containing common divisors 
    of n1 and n2 """
    divisors = () # the empty tuple
    for i in range(1, min(n1,n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors

# Lists
"""
# Look a lot like tuples
– Ordered sequence of values, each identified by an index	
– Use [1, 2, 3]	rather than (1,	2, 3)	
– Singletons are now just [4] rather than (4, )	
# BIG DIFFERENCE	
– Lists	are mutable!! 
– While	tuple, int, float, str are immutable	
– So lists can be modified aMer they are created! 
"""
# examples
## universities

Techs = ['MIT', 'Cal Tech']
Ivys = ['Harvard', 'Yale', 'Brown']

Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Cal Tech'], ['Harvard', 'Yale', 'Brown']]

Techs.append('RPI') # append has a side effect: it doesn't create a new list, 
# it mutates the existing one to add a new element to the end

Univs[1].append('API')
print Univs
print Ivys


print('Univs = ')
print(Univs)
print('')
print('Univs1 =')
print(Univs1)

for e in Univs:
    print('Univs contains ')
    print(e)
    print('   which contains')
    for u in e:
        print('      ' + u)

# Observations
"""
- Elements of Univs are	not copies of the lists to which Techs and
Ivys are bound, but are the lists themselves!	
- This effect is called aliasing:
    > One through the variable Techs
    > A second through the first element of list objects to which Univs is bound
- Can mutate object through either path, but effect will be visible through both
- Convenient but treacherous
"""

# more methods in list. see https://docs.python.org/2/tutorial/datastructures.html
# example
# remove items from L1 that are both in L1 and L2
def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)


L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1, L2)
print(L1) # returns [2, 3, 4]

# Why failed to remove the 2, which is also a duplicate?
# Reason: 
"""
Inside for loop, Python keeps track of where it is in list using internal counter.
When we mutate a list, we change its length but Python doesn't update counter
"""
# Better Solutions: Cloning the list
def removeDupsBetter(L1, L2):
    L1Start = L1[:]
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDupsBetter(L1, L2)
print(L1)

# Functions as objects
# functions are first class object, which means you can treat them the same way 
# you treat number, string, tuple, list, and dictionary.
# - They have types
# - They can be elements of data structures like lists
# - They can appear in expressions
#     > As part of an assignment statement
#     > As an argument to a function!!
# Particular useful to use functions as arguments when coupled with lists
# - Aka higher order programming
"""
What is Higher Order Programming?

From Wikipedia

    Higher-order programming is a style of computer programming that uses
    software components, like functions, modules or objects, as values. 
    It is usually instantiated with, or borrowed from, models of computation
    such as lambda calculus which make heavy use of higher-order functions.
    
    For example, in higher-order programming, one can pass functions as
    arguments to other functions and functions can be the return value of other
    functions (such as in macros or for interpreting). This style of programming
    is mostly used in functional programming, but it can also be very useful in
    object-oriented programming. A slightly different interpretation of
    higher-order programming in the context of object-oriented programming are
    higher order messages, which let messages have other messages as arguments,
    rather than functions.
"""
