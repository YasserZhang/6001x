#iterative vs. recursive
# in iterative procedure, we initialize a variable, then we add, multiply, 
# minus or divide a target array of values one by one and assignment the result
# each time to the variable we initialized. After the procedure finished, we return
# the variable which store the final result of the iterative manipulation.
# example
def iterMul(a, b):
    result = 0
    while b > 0:
        result += a # update the varaible result each time
        b -= 1
    return result # return the final result
# In recursive procedure, we reduce a problem to a simpler or smaller version 
# of the same problem, plus some simple computations, then keep reducing until
# reach a simple case that can be solved directly.
# So a recursive procedure includes two parts: base case and recursive step.
# The base case should garantee recursive steps will reach a final step, which 
# can be any fixed value.
# example
def recurMul(a, b):
    if b == 1:
        return a # base case
    else:
        return a + recurMul(a, b-1) # recursive steps
"""
Some Observations
- Each recursive call to a function creates its own environment, with local scoping
variables
- Bindings for variable in each frame distinct, and not changed by recursive call
- Flow of control will pass back to earlier frame once function call returns value
"""
"""
understanding recursive functions with inductive reasoning
- Base case, we can show that recurMul must return correct answer
- For recursive case, we can assume that recurMul correctly returns an answer for 
problems of size smaller than b, then by the addition step, it must also return 
a correct answer for problem of size b
- Thus by induction, code correctly returns answer
"""
# comparing iterative and recursive methods on factorial function
# iterative
def factI(n):
    """assumes that n is an int > 0 return n!"""
    res = 1
    while n > 1:
        res = res*n
        n -= 1
    return res

# recursive
def factR(n):
    """assumes that n is an int > 0 return n!"""
    if n == 1:
        return n
    return n*factR(n-1)

# Tower of Hanoi
# think recursively
# Solve a small problem
# Solve a basic problem
# Solve a small prblem
"""
If we have n discs to move, we can treat the stack as one disc and n-1 discs,
then we can manage to move away the n-1 discs on the disc at the bottom to a 
spare spike, then we put the bottom disc to the target spike. Finishing these steps,
we can again treat the rest of discs as one disc and n-2 discs and repeat the previous
steps again and again until the last and the smallest disc.
"""
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))
    def Towers(n, fr, to, spare):
        if n == 1:
            printMove(fr, to)
        else:
            Towers(n-1, fr, spare, to)
            Towers(1, fr, to, spare)
            Towers(n-1, spare, to, fr)


# Fibonachi numbers
def fib(x):
    """assumes x an int >= 0
        returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        

# Recursion on non-numerics
# checking if a string of characters is a palindrome, i.e., reads the same forwards and backwards
def isPalindrome(s):
    # filter off non-characters from the string and converts it to lowercase characters
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    #checking palindrome recursively
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))
    
     
# global variable. A global variable is a variable that can be mutated at any 
# environment, which means it is not subject to locality of code. 
"""
Use with care!!
Destroy locality of code
Since can be modified or read in a wide range of places, can be easy to break 
locality and introduce bugs!!
"""
def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)


def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('fib called ' + str(numCalls) + ' times')

