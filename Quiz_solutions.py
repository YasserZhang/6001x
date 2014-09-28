"""
create a log function to calculate the logarithm of a number x relative to a base b.
pyseudo code:
    p = 1
    exponent function(b,n):
        calculate the product of a number multiplied by itself n times.
        return p = p * the product
        
    myLog function (x,b):
        res = exponent function(b,n)
        base case:
            if res is greater than x
                return 0
            if b is equal to x
                return 1
        recursion:
            else: 1 + exponent function(b,n+1)

"""

def myLog(x,b):
    # calculate the exponent of a number raised to n.
    def exponent(b,n):
        if n == 0:
            return 1
        else:
            return b*exponent(b,n-1)

    # use recursion to calculate the logarithm of a number,
    # if the exponent of a number raised to n is greater than x,
    # then stop the recursion and return the base value 0, if equal,
    # then return 1
    def log_b(n):
        p = exponent(b,n)
        print p
        if p > x:
            return 0
        elif p == x:
            return 1
        else:
            return 1 + log_b(n+1)
    return log_b(0) -1

print myLog(1,2)

# using iterative methods, which is much more better than recursion in this case.

def myLog(x,b):
    count = 0 
    exponent = b
    while exponent <= x:
        exponent *=b
        count += 1
    return count

print myLog(256,2)

"""
interlace characters of two strings,
1, find the minimun length of two strings,
2, iterate through the range of minimun length
    to concatenate two characters having the same index in each string.
3, add the rest part of the longer string to the end of the new string.
"""


def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    length = min(len(s1),len(s2))
    newString = ''
    for i in range(length):
        newString = newString + s1[i] + s2[i]
    newString = newString + s1[length:] + s2[length:]
    return newString

a = 'hello'
b = 'myworld'
print laceStrings(b,a)
            
    